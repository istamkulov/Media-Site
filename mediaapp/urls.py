from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'sources', SourceViewSet)
router.register(r'movie-sources', MovieSourceViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = router.urls