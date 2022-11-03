from django import forms
from contact.models import Contact
from tinymce.widgets import TinyMCE

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["read", "created", "updated"]