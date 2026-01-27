from celery import shared_task
from .models import Source
import requests
from django.utils import timezone

@shared_task
def check_source_availability(source_id):
    try:
        src = Source.objects.get(pk=source_id)
    except Source.DoesNotExist:
        return {"error": "not found"}
    try:
        r = requests.head(src.url, timeout=10, allow_redirects=True)
        src.last_checked = timezone.now()
        src.is_active = r.status_code == 200
        src.save(update_fields=["last_checked", "is_active"])
        return {"id": source_id, "status": r.status_code}
    except Exception as e:
        src.last_checked = timezone.now()
        src.is_active = False
        src.save(update_fields=["last_checked", "is_active"])
        return {"id": source_id, "error": str(e)}

@shared_task
def check_all_sources():
    qs = Source.objects.all()
    results = []
    for src in qs:
        results.append(check_source_availability.delay(src.id))
    return {"dispatched": len(results)}

@shared_task
def import_media_task(shows_url=None, movies_url=None):
    from django.core import management
    management.call_command("import_media", ({"shows_url": shows_url} if shows_url else {} , ({"movies_url": movies_url} if movies_url else {})))