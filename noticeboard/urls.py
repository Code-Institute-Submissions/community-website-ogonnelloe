from . import views
from django.urls import path

urlpatterns = [
    path('', views.Noticeboard.as_view(), name='noticeboard'),
    path('add_notice/', views.AddNotice.as_view(), name='add_notice'),
    ]