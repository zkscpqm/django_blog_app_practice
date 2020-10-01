from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created. You can now log in..')
            return redirect('blog-login')
        messages.warning(request, f'Account registration failed.')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_form,
        'profile_update_form': profile_form
    }

    return render(request, 'users/profile.html', context=context)
