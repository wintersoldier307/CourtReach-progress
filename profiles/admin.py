from django.contrib import admin
from .models import PlayerProfile


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'country', 'visibility_score')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'country')
    list_filter = ('position', 'country', 'playing_level')
