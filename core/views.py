from django.shortcuts import render
from profiles.models import PlayerProfile


def home(request):
    players = PlayerProfile.objects.filter(visibility_score__gt=0)[:8]
    context = {'players': players}
    return render(request, 'core/home.html', context)
