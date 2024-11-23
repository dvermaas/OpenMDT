from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("announcement/<int:pk>/", views.announcement, name="announcement"),
]
