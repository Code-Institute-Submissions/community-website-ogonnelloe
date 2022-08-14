from django.contrib import admin
from .models import Notice
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Notice)
class NoticeAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('title', 'contact_email', 'created_on', 'approved')
    search_fields = ['title', 'description']
    actions = ['approve_notices']

    def approve_notices(self, request, queryset):
        queryset.update(approved=True)
