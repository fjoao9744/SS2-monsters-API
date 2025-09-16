from django.urls import path
from .views import Monsters_v1, Monsters_info_v1

urlpatterns = [
    path("v1/", Monsters_v1.as_view()),
    path("v1/info/", Monsters_info_v1.as_view())
]
