from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.table, name="report_tabulated"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("create/", views.ReportCreateView.as_view(), name="create"),
    path("create2/", views.form, name="create2"),
    path("<int:pk>/createsuspect", views.add_suspect_to_report, name="addsuspect"),
    path("edit/<int:pk>/", views.detail_info_form, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
