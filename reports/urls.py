from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("create/", views.ReportCreateView.as_view(), name="create"),
    # path(
    #     "create/<int:pk>/",
    #     views.ReportSuspectCreateView.as_view(),
    #     name="create",
    # ),
    path("<int:pk>/createsuspect", views.add_suspect_to_report, name="addsuspect"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
