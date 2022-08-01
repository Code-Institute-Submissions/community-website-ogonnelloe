from .views import CommunityUpdatesMostRecent
from django.urls import path

urlpatterns = [
    path('', CommunityUpdatesMostRecent.as_view(), name='home'),
]