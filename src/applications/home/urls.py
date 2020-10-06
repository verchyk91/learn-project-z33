from django.urls import path

from src.applications.home.apps import HomeConfig
from src.applications.home.views import IndexView

app_name = HomeConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
