from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("", include("articles.urls")),
    path("contact/", include("contact.urls")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Meridian"
admin.site.site_title = "Meridian"
admin.site.index_title = "Welcome :)"