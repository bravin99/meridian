from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


def profile(request):
    user = request.user
    context = {}
    return render(request, "accounts/profile.html", context)
