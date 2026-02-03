import requests
from datetime import date
from django.core.management.base import BaseCommand
from mediaapp.models import Movie, Source, MovieSource

API_URL = "https://channelsapi.s3.amazonaws.com/media/test/movies.json"

class Command(BaseCommand):
    help = "Импорт фильмов из API с источниками"

    def handle(self, *args, **kwargs):
        try:
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Ошибка запроса к API: {e}"))
            return

        try:
            data = response.json()
        except ValueError:
            self.stdout.write(self.style.ERROR("Ошибка при разборе JSON"))
            return

        imported_count = 0

        for item in data:
            title = item.get("name")
            if not title:
                continue

            description = item.get("description", "")
            image = item.get("image", "")
            bg_image = item.get("bg_image", "")
            imdb_rating = str(item.get("imdb_rating", ""))
            #kinopoisk_rating = ""
            release_year = item.get("release_year")
            runtime = item.get("runtime", None)
            rating = item.get("rating", "")

            if image.startswith("//"):
                image = "https:" + image
            if bg_image.startswith("//"):
                bg_image = "https:" + bg_image

            release_date = None
            if release_year:
                try:
                    release_date = date(int(release_year), 1, 1)
                except Exception:
                    release_date = None

            movie, created = Movie.objects.update_or_create(
                title=title,
                defaults={
                    "description": description,
                    "image": image,
                    "imdb": imdb_rating,
                    "release_date": release_date,
                }
            )

            sources_data = item.get("modes", {}).get("web_sources", {}).get("subscriptions", [])
            for s in sources_data:
                name = s.get("name")
                if not name:
                    continue
                url = s.get("subscription_code", name)

                source, _ = Source.objects.get_or_create(
                    url=url,
                    defaults={"name": name}
                )

                MovieSource.objects.update_or_create(
                    movie=movie,
                    source=source,
                    defaults={
                        "quality": "",
                        "language": "",
                    }
                )

            imported_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Импортировано фильмов: {imported_count}"))
