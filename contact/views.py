from django.shortcuts import render, redirect
from contact.models import Contact
from contact.forms import ContactForm
from django.contrib import messages

from django.views.generic import CreateView


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact/contact.html"
    
    def get_success_url(self) -> str:
        messages.success(self.request, "Contact submitted successfully")
        return redirect(self.request.path_info)