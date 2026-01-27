from django.contrib import admin
from django.urls import path, include

from mediaapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("mediaapp.urls")),
    path('',index,name="index"),
]
