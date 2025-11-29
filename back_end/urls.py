from django.urls import path
from .views import \
Monsters_v1, Monsters_filter_v1, Monsters_info_v1, Monsters_filter_info_v1
from .views import \
Monsters_v2, Monsters_filter_v2, Monsters_info_v2, Monsters_filter_info_v2

urlpatterns = [
    path("v1/info/<str:family>/", Monsters_filter_info_v1.as_view()),
    path("v1/info/", Monsters_info_v1.as_view()),
    
    path("v1/<str:family>/<str:monster>/", Monsters_filter_v1.as_view()),
    path("v1/<str:family>/", Monsters_filter_v1.as_view()),
    path("v1/", Monsters_v1.as_view()),
    
    path("v2/info/<str:family>/", Monsters_filter_info_v2.as_view()),
    path("v2/info/", Monsters_info_v2.as_view()),
    
    path("v2/<str:family>/<str:monster>/", Monsters_filter_v2.as_view()),
    path("v2/<str:family>/", Monsters_filter_v2.as_view()),
    path("v2/", Monsters_v2.as_view())
]
