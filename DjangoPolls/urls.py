from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import include, path
from django.views.generic.base import TemplateView, RedirectView
from .api import api

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("reports/", include(("reports.urls", "reports"), "reports")),
    path("profiles/", include(("profiles.urls", "profiles"), "profiles")),
    path("api/", api.urls),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
