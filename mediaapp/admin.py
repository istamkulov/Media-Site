from django.contrib import admin
from django.utils.html import format_html
from .models import Movie, Source, MovieSource, Show, Season, Episode

class MovieSourceInline(admin.TabularInline):
    model = MovieSource
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'release_date', 'imdb', 'kinopoisk', 'sources_count')
    search_fields = ('title', 'description', 'imdb', 'kinopoisk')
    list_filter = ('release_date', 'imdb')

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="70" style="object-fit:cover; border-radius:3px;" />',
                obj.image
            )
        return "-"
    thumbnail.short_description = 'Фото'

    def sources_count(self, obj):
        return obj.sources.count()
    sources_count.short_description = 'Источников'

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active')
    search_fields = ('name', 'url')

@admin.register(MovieSource)
class MovieSourceAdmin(admin.ModelAdmin):
    list_display = ('movie', 'source', 'quality', 'language')

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('show', 'number')

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'number', 'title')
