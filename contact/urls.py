from django.urls import path
from contact import views

urlpatterns = [
    path("", views.ContactCreateView.as_view(), name="contact"),
]