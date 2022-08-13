from .views import CommunityUpdatesMostRecent, plan_page, exchange_page, CommunityUpdateList, CommunityUpdateDetail
from django.urls import path

urlpatterns = [
    path('', CommunityUpdatesMostRecent.as_view(), name='home'),
    path('community_updates', CommunityUpdateList.as_view(), name='community_update_list'),
    path('community_updates/<slug:slug>', CommunityUpdateDetail.as_view(), name='community_update_detail'),
    path('3-yaer-plan', plan_page, name='plan_page'),
    path('exchange', exchange_page, name='exchange_page'),
]