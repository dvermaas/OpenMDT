from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from accounts import views as accounts_views
from .api import api

urlpatterns = [
    # path("", TemplateView.as_view(template_name="accounts/home.html"), name="home"),
    path("", accounts_views.index, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include(("accounts.urls", "accounts"), "accounts")),
    path("allauth/", include("allauth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("reports/", include(("reports.urls", "reports"), "reports")),
    path("profiles/", include(("profiles.urls", "profiles"), "profiles")),
    path(
        "legislations/", include(("legislations.urls", "legislations"), "legislations")
    ),
    path("common/", include(("common.urls", "common"), "common")),
    path("api/", api.urls),
    path("favicon.ico", RedirectView.as_view(url="/templates/favicon.ico")),
    path("silk/", include("silk.urls", namespace="silk")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
