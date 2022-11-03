from django.shortcuts import render, redirect
from contact.models import Contact
from contact.forms import ContactForm
from django.contrib import messages

from django.views.generic import CreateView


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact/contact.html"
    
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Contact sent successfully")
        return redirect("contact")