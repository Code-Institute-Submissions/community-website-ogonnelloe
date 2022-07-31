from django.shortcuts import render
from django.views import generic
from .models import CommunityUpdate

class UpdateList(generic.ListView):
    model = CommunityUpdate
    queryset = CommunityUpdate.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


