from django.contrib import admin
from .models import CommunityUpdate, CommunityUpdateComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CommunityUpdate)
class CommunityUpdateAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    summernote_fields = "content"


@admin.register(CommunityUpdateComment)
class CommunityUpdateCommentAdmin(SummernoteModelAdmin):

    list_filter = ("approved", "created_on")
    list_display = ("commenter", "body", "post", "created_on", "approved")
    search_fields = ["name", "body"]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
