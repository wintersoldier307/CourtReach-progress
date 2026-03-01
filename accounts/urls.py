from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # scout profile
    path('scout/profile/', views.scout_profile, name='scout_profile'),
    path('scout/profile/edit/', views.edit_scout_profile, name='edit_scout_profile'),
    # admin dashboard
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/players/', views.admin_players, name='admin_players'),
    path('admin/player/<int:user_id>/', views.admin_player_detail, name='admin_player_detail'),
    path('admin/scouts/', views.admin_scouts, name='admin_scouts'),
    path('admin/scout/<int:user_id>/', views.admin_scout_detail, name='admin_scout_detail'),
    path('admin/unverified/', views.unverified_scouts, name='unverified_scouts'),
    path('admin/verify/<int:user_id>/', views.verify_scout, name='verify_scout'),
]
