from django.db import models
from django.conf import settings


class Watchlist(models.Model):
    scout = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watchlists')
    player = models.ForeignKey('profiles.PlayerProfile', on_delete=models.CASCADE, related_name='watched_by')
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('scout', 'player')

    def __str__(self):
        return f"{self.scout.username} -> {self.player.user.username}"
