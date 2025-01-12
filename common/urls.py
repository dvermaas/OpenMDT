from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("downloads/<int:pk>/", views.downloads, name="downloads"),
]
