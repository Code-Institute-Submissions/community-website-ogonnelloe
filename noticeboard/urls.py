from . import views
from django.urls import path

urlpatterns = [
    path('noticeboard/', views.Noticeboard.as_view(), name='noticeboard'),
    path('noticeboard/add_notice/', views.AddNotice.as_view(), name='add_notice'),
    ]