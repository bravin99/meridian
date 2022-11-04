from django.contrib.sitemaps import Sitemap
from articles.models import Article

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Article.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()