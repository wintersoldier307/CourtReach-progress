from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.my_profile, name='my_profile'),
    path('me/edit/', views.edit_profile, name='edit_profile'),
    path('player/<int:user_id>/', views.player_detail, name='player_detail'),
]