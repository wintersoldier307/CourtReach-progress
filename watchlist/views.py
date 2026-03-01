from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Watchlist
from profiles.models import PlayerProfile


@login_required
@user_passes_test(lambda u: u.role == 'SCOUT' and u.is_verified)
def watchlist_view(request):
    items = Watchlist.objects.filter(scout=request.user)
    return render(request, 'watchlist/list.html', {'items': items})

@login_required
@user_passes_test(lambda u: u.role == 'SCOUT' and u.is_verified)
def add_watchlist(request, profile_id):
    profile = get_object_or_404(PlayerProfile, id=profile_id)
    Watchlist.objects.get_or_create(scout=request.user, player=profile)
    return redirect('search_players')

@login_required
@user_passes_test(lambda u: u.role == 'SCOUT' and u.is_verified)
def remove_watchlist(request, item_id):
    item = get_object_or_404(Watchlist, id=item_id, scout=request.user)
    item.delete()
    return redirect('watchlist')
