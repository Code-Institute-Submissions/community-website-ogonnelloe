from .models import Notice
from django import forms


class NoticeForm(forms.ModelForm):
    # Telling CommentForm what model to use and what fields to show in form
    class Meta:
        model = Notice
        fields = (
            "title",
            "description",
            "contact_number",
            "contact_email",
            "location",
            "background_image",
        )
