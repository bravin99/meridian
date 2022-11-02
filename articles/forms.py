from django import forms
from articles.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['parent', 'message']