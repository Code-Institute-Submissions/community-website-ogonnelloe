from . import views
from django.urls import path

urlpatterns = [
    path('', views.CommunityUpdatesMostRecent.as_view(), name='home'),
    path('community_updates', views.CommunityUpdateList.as_view(), name='community_update_list'),
    path('community_updates/<slug:slug>', views.CommunityUpdateDetail.as_view(), name='community_update_detail'),
    path('like/<slug:slug>', views.CommunityUpdateLike.as_view(), name='community_update_like'),
    path('3-yaer-plan', views.plan_page, name='plan_page'),
    path('exchange', views.exchange_page, name='exchange_page'),
]