from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import CustomUser
from .forms import UserRegistrationForm, ScoutProfileForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'home'


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


# Scout profile functions

@login_required
@user_passes_test(lambda u: u.role == 'SCOUT')
def scout_profile(request):
    return render(request, 'accounts/scout_profile.html', {'scout': request.user})


@login_required
@user_passes_test(lambda u: u.role == 'SCOUT')
def edit_scout_profile(request):
    if request.method == 'POST':
        form = ScoutProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('scout_profile')
    else:
        form = ScoutProfileForm(instance=request.user)
    return render(request, 'accounts/edit_scout_profile.html', {'form': form})


# admin functions

def admin_required(view_func):
    from django.contrib.auth.decorators import user_passes_test
    return user_passes_test(lambda u: u.is_superuser)(view_func)


@admin_required
def admin_dashboard(request):
    from profiles.models import PlayerProfile
    players_count = PlayerProfile.objects.count()
    scouts_count = CustomUser.objects.filter(role=CustomUser.SCOUT).count()
    unverified_count = CustomUser.objects.filter(role=CustomUser.SCOUT, is_verified=False).count()
    return render(request, 'accounts/admin_dashboard.html', {
        'players_count': players_count,
        'scouts_count': scouts_count,
        'unverified_count': unverified_count
    })


@admin_required
def admin_players(request):
    from profiles.models import PlayerProfile
    players = PlayerProfile.objects.all().order_by('-visibility_score')
    return render(request, 'accounts/admin_players.html', {'players': players})


@admin_required
def admin_player_detail(request, user_id):
    from profiles.models import PlayerProfile
    profile = get_object_or_404(PlayerProfile, user__id=user_id)
    return render(request, 'accounts/admin_player_detail.html', {'profile': profile})


@admin_required
def admin_scouts(request):
    scouts = CustomUser.objects.filter(role=CustomUser.SCOUT)
    return render(request, 'accounts/admin_scouts.html', {'scouts': scouts})


@admin_required
def admin_scout_detail(request, user_id):
    scout = get_object_or_404(CustomUser, id=user_id, role=CustomUser.SCOUT)
    return render(request, 'accounts/admin_scout_detail.html', {'scout': scout})


@admin_required
def unverified_scouts(request):
    scouts = CustomUser.objects.filter(role=CustomUser.SCOUT, is_verified=False)
    return render(request, 'accounts/unverified_scouts.html', {'scouts': scouts})


@admin_required
def verify_scout(request, user_id):
    scout = get_object_or_404(CustomUser, id=user_id, role=CustomUser.SCOUT)
    scout.is_verified = True
    scout.save()
    return redirect('unverified_scouts')
