from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from articles.forms import CommentForm
from articles.models import Article, Comments, Favourite


class ArticleListView(ListView):
    queryset = Article.objects.filter(publish=True)
    template_name = "articles/articles.html"
    context_object_name = "objects"
    paginate_by = 12

class ArticleDetailView(DetailView):
    queryset = Article.objects.filter(publish=True)
    template_name = "articles/article_detail.html"
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["related"] = Article.objects.filter(publish=True, tags__in=obj.tags.all()
            ).exclude(pk=obj.pk).order_by("-created")[:5]
        
        context["comment_form"] = CommentForm()
        context["comments"] = Comments.objects.filter(parent_article=obj)
        
        user = self.request.user
        if user.is_authenticated:
            context["is_fav"] = Favourite.objects.filter(user=user, fav_article=obj).exists()
        
        return context

    def post(self, request, *args, **kwags):
        if self.request.method == "POST":
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                user = self.request.user
                message = comment_form.cleaned_data["message"]
                try:
                    parent = comment_form.cleaned_data["parent"]
                except:
                    parent = None
            new_comment = Comments(
                parent_article = self.get_object(), user=user, message=message, parent=parent
            )
            new_comment.save()
            return redirect(self.request.path_info)

def tagged(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    objects = Article.objects.filter(
        tags=tag, publish=True
    )
    return render(request, "articles/tagged.html", context={
        "tag":tag, "objects":objects
    })

@login_required
def favourite_articles(request, slug):
    user = request.user
    tutorial = Article.objects.get(slug=slug)
    try:
        fav = Favourite.objects.get(user=user, fav_article=tutorial)
        fav.delete()
        messages.success(request, 'Removed from favourites!')
    except ObjectDoesNotExist:
        fav = Favourite(user=user, fav_article=tutorial)
        fav.save()
        messages.success(request, 'Added to favourites!')
        
    return redirect(tutorial.get_absolute_url())

class ArticleSearchView(ListView):
    queryset = Article.objects.filter(publish=True)
    template_name = "articles/search.html"
    context_object_name = 'objects'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        objects = Article.objects.filter(
                title__icontains=query, publish=True
            ).order_by('-created')
        return objects
