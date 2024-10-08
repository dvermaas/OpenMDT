from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table", views.table, name="tabulated"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    # path("create/", views.ReportCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", views.detail_info_form, name="edit"),
    path("edit-summary/<int:pk>/", views.detail_summary_form, name="editsummary"),
    path("edit-picture/<int:pk>/", views.detail_picture_form, name="editpicture"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("test/", views.test, name="test"),
]
