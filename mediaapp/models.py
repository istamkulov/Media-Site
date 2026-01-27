from django.db import models

class Source(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or self.url


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    imdb = models.CharField(max_length=50, blank=True)
    kinopoisk = models.CharField(max_length=50, blank=True)
    release_date = models.DateField(null=True, blank=True)
    sources = models.ManyToManyField('Source', through='MovieSource')

    def __str__(self):
        return self.title


class MovieSource(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    quality = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} — {self.source.name}"


class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    imdb = models.CharField(max_length=50, blank=True)
    kinopoisk = models.CharField(max_length=50, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='seasons')
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['number']
        unique_together = ('show', 'number')

    def __str__(self):
        return f"{self.show.title} — Сезон {self.number}"


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.season.show.title} S  {self.season.number}E{self.number}"
