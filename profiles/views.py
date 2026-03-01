from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PlayerProfile
from .forms import PlayerProfileForm

def player_detail(request, user_id):
    # only verified scouts can view any player
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role != 'SCOUT' or not request.user.is_verified:
        return redirect('home')
    profile = get_object_or_404(PlayerProfile, user__id=user_id)
    return render(request, 'profiles/detail.html', {'profile': profile})

@login_required
@user_passes_test(lambda u: u.role == 'PLAYER')
def my_profile(request):
    profile, created = PlayerProfile.objects.get_or_create(user=request.user)
    return render(request, 'profiles/my_profile.html', {'profile': profile})

@login_required
@user_passes_test(lambda u: u.role == 'PLAYER')
def edit_profile(request):
    profile, created = PlayerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = PlayerProfileForm(instance=profile)
    return render(request, 'profiles/edit.html', {'form': form})
