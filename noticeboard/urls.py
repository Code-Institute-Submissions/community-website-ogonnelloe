from . import views
from django.urls import path

urlpatterns = [
    path('', views.Noticeboard.as_view(), name='noticeboard'),
    path('add_notice/', views.AddNotice.as_view(), name='add_notice'),
    path('<pk>/delete/', views.DeleteNotice.as_view(), name='delete_notice'),
    path('<pk>/update/', views.UpdateNotice.as_view(), name='update_notice'),
    ]