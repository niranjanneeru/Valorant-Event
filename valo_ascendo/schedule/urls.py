from django.urls import path

from .views import (
    schedule_view
)

app_name = "game"
urlpatterns = [
    path("", view=schedule_view, name="schedule"),
]
