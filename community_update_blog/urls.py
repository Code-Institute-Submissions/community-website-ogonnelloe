from .views import CommunityUpdatesMostRecent, plan_page, exchange_page
from django.urls import path

urlpatterns = [
    path('', CommunityUpdatesMostRecent.as_view(), name='home'),
    path('3-yaer-plan', plan_page, name='plan_page'),
    path('exchange', exchange_page, name='exchange_page'),
]