from django.contrib import admin
from .models import CommunityUpdate
from django_summernote.admin import SummernoteModelAdmin

@admin.register(CommunityUpdate)
class CommunityUpdateAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')