from django.urls import path

from .views import (

)

app_name = "game"
urlpatterns = [
    path("next/", view=question_view, name="question"),
    path("code/", view=code_view, name='code')

]
