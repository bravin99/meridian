from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, ListView
from taggit.models import Tag

from articles.models import Article, Comments, Favourite
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    queryset = Article.objects.filter(publish=True)
    template_name = "articles/articles.html"
    context_object_name = "objects"
    paginate_by = 12