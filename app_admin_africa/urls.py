from django.urls import path
from . import views


urlpatterns = [
path('home/', views.home, name='home'),
path('', views.index, name='index_admin'),
path('save/', views.save_data, name='save'),
path('delete/', views.delete_data, name='delete'),
path('edit/', views.edit_data, name='edit'),





]