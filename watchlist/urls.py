from django.urls import path
from . import views

urlpatterns = [
    path('', views.watchlist_view, name='watchlist'),
    path('add/<int:profile_id>/', views.add_watchlist, name='add_watchlist'),
    path('remove/<int:item_id>/', views.remove_watchlist, name='remove_watchlist'),
]