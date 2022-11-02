from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from articles.models import Favourite, Article
from accounts.models import Profile
from django.views.generic import TemplateView

from accounts.forms import UserUpdateForm, ProfileForm

from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def profile(request):
    user = request.user
    favorites = Favourite.objects.filter(user=user)
    articles = Article.objects.filter(publish=True).order_by("-created")

    favs = []
    for fav in favorites:
        for a in articles:
            if fav.fav_article == a:
                favs.append(a)

    context = {
        "favs": favs,
    }
    return render(request, "accounts/profile.html", context)

def settings(request):
    user = get_object_or_404(User, username=request.user.username)
    profile = get_object_or_404(Profile, user=user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/settings.html", context)