from django.contrib import admin
from articles.models import Favourite, Article, Comments

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'created',]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created', 'updated', 'tags']
    search_fields = ['title', 'author', 'tags']
    
admin.site.register(Favourite)
admin.site.register(Comments)