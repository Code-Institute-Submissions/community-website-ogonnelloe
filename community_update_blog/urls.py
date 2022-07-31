from .views import UpdateList
from django.urls import path

urlpatterns = [
    path('', UpdateList.as_view(), name='home'),
]