from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index")
# ]


urlpatterns = [
    path("", views.index, name="index"),
    path(r"title/<title>", views.title, name="title")
]
