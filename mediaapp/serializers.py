from rest_framework import serializers
from .models import *

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

class MovieSourceSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)

    class Meta:
        model = MovieSource
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    sources = MovieSourceSerializer(source='moviesource_set', many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = "__all__"

class ShowSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = "__all__"
