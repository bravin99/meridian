from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)
