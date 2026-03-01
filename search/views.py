from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from profiles.models import PlayerProfile


@login_required
@user_passes_test(lambda u: u.role == 'SCOUT' and u.is_verified)
def search_players(request):
    qs = PlayerProfile.objects.filter(visibility_score__gt=0)
    position = request.GET.get('position')
    age_min = request.GET.get('age_min')
    age_max = request.GET.get('age_max')
    country = request.GET.get('country')
    playing_level = request.GET.get('playing_level')
    min_ppg = request.GET.get('min_ppg')

    if position:
        qs = qs.filter(position__icontains=position)
    if age_min:
        qs = qs.filter(age__gte=age_min)
    if age_max:
        qs = qs.filter(age__lte=age_max)
    if country:
        qs = qs.filter(country__icontains=country)
    if playing_level:
        qs = qs.filter(playing_level__icontains=playing_level)
    if min_ppg:
        qs = qs.filter(ppg__gte=min_ppg)

    qs = qs.order_by('-visibility_score')
    return render(request, 'search/results.html', {'players': qs})
