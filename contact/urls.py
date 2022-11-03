from django.urls import path
from contact import views

urlpatterns = [
    path("core/contact/", views.ContactCreateView.as_view(), name="contact"),
]