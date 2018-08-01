from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import UserForm, ProfileForm
from accounts.models import User
from . import forms




class SignUp(CreateView):
    model = User
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/updateprofile.html'



class UpdateProfile(UpdateView):

    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


    def update_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, _('Your profile was successfully updated!'))
                return redirect('directory:home')
            else:
                messages.error(request, _('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'profiles/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


