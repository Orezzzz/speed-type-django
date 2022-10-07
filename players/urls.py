from django.urls import re_path
from players import views



urlpatterns=[
    re_path(r'^players$',views.playersApi),
    re_path(r'^players/([0-9]+)$',views.playersApi)
]