from django.db import models
from django.conf import settings


class PlayerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='player_profiles/', null=True, blank=True)
    position = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    social_medias = models.TextField(blank=True)

    playing_level = models.CharField(max_length=100, blank=True)
    availability = models.BooleanField(default=True)
    ppg = models.FloatField(null=True, blank=True)
    rpg = models.FloatField(null=True, blank=True)
    apg = models.FloatField(null=True, blank=True)
    highlight_video_url = models.URLField(blank=True)
    visibility_score = models.IntegerField(default=0)

    def calculate_visibility(self):
        # simple scoring: add 1 point for each filled field
        score = 0
        fields = [
            self.position,
            self.height,
            self.weight,
            self.age,
            self.country,
            self.telephone,
            self.email,
            self.social_medias,
            self.playing_level,
            self.ppg,
            self.rpg,
            self.apg,
            self.highlight_video_url,
        ]
        for f in fields:
            if f:
                score += 1
        return score

    def get_completion_percentage(self):
        return int((self.visibility_score / 13) * 100)

    def save(self, *args, **kwargs):
        self.visibility_score = self.calculate_visibility()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} Profile"

