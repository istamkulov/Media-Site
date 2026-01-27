from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class MovieSourceViewSet(viewsets.ModelViewSet):
    queryset = MovieSource.objects.all()
    serializer_class = MovieSourceSerializer

class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer



def index(request):
    movies = Movie.objects.all()
    return render(request,"mediaapp/index.html",{"movies":movies})
