from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:profile_id>/", views.detail, name="detail"),
    # path("create/", views.ReportCreateView.as_view(), name="create"),
    # path("edit/<int:report_id>/", views.edit, name="edit"),
    path("delete/<int:profile_id>/", views.delete, name="delete"),
]
