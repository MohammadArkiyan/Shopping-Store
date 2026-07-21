from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, ManualSignupForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)  # session expires on browser close
            messages.success(request, "Login was successful.")
            return redirect('shopping_store:index')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request, 'Your logout was successful.')
    return redirect('account:user_login')




def user_signup(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration was successful.")
            return redirect('shopping_store:index')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def profile_view(request):

    profile, created = Profile.objects.get_or_create(user=request.user)


    if request.method == 'POST':


        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('account:profile')


    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile,
    }

    return render(request, 'account/profile.html', context)

