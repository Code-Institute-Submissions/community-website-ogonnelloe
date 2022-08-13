from .models import CommunityUpdateComment
from django import forms


class CommentForm(forms.ModelForm):
    # Telling CommentForm what model to use and what fields to show in form
    class Meta:
        model = CommunityUpdateComment
        fields = ('body',)
