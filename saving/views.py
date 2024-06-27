from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

def home_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'account/index.html')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile': profile})
