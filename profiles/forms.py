from django import forms
from .models import PlayerProfile


class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        exclude = ('user', 'visibility_score')
