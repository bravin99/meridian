from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from configs.sitemaps import ArticleSitemap

sitemaps = {
    'article': ArticleSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("", include("articles.urls")),
    path("contact/", include("contact.urls")),

    path("sitemaps.xml", sitemap, {
        'sitemaps': sitemaps,
    }, name="meridian_sitemaps"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Meridian"
admin.site.site_title = "Meridian"
admin.site.index_title = "Welcome :)"