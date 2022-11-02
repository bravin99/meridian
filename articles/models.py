from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from tinymce.models import HTMLField

User = get_user_model()

class ContentAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TaggedArticle(TaggedItemBase):
    content_object = models.ForeignKey('Article', on_delete=models.CASCADE)
    

def featured_image_path(instance, filename):
    return "articles/{0}/{1}".format(instance, filename)

class Article(ContentAppBaseModel):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, max_length=160)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to=featured_image_path)
    content = HTMLField()
    tags = TaggableManager(through=TaggedArticle)
    publish = models.BooleanField(default=True)
    views = models.PositiveIntegerField(blank=True, null=True, editable=False)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'article_detail', kwargs={
                'year': self.created.strftime('%Y'),
                'month': self.created.strftime('%m'),
                'day': self.created.strftime('%d'),
                'author':self.author,'slug': self.slug
                }
        )
    
    class Meta:
        ordering = ['-created',]
        
class Comments(ContentAppBaseModel):
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    message = models.TextField(max_length=100)
    display = models.BooleanField(default=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    
    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse()
    
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
    def __str__(self):
        return f"Comment by {self.user.username}"
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Comments'
        verbose_name_plural = verbose_name
        
class Favourite(ContentAppBaseModel):
    fav_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    
    def __str__(self):
        return f"{self.fav_article} - {self.user.username}"
    
    class Meta:
        ordering = ['-created',]
