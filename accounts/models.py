from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    PLAYER = 'PLAYER'
    SCOUT = 'SCOUT'

    ROLE_CHOICES = [
        (PLAYER, 'Player'),
        (SCOUT, 'Scout'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='scout_profiles/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # players are automatically verified
        if self.role == self.PLAYER:
            self.is_verified = True
        # superusers must always be verified
        if self.is_superuser:
            self.is_verified = True
        super().save(*args, **kwargs)
