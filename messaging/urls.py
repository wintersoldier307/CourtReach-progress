from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversation/<int:user_id>/', views.conversation, name='conversation'),
]