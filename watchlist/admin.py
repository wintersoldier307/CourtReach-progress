from django.contrib import admin
from .models import Watchlist


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('scout', 'player', 'created_at')
    search_fields = ('scout__username', 'player__user__username')
