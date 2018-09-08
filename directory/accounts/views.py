from django.shortcuts import render_to_response
from django.http import HttpResponse, request
# from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from accounts.forms import UserForm, ProfileForm
from accounts.models import Profile
from . import forms


class SignUp(CreateView):
    model = Profile
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'


class UpdateProfile(UpdateView):
    model = Profile
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    form_class = ProfileForm

    # form_classes = {'user': UserForm,
    #                 'profile': ProfileForm}

    def get_success_url(self):
        return reverse('home')

    def get_object(self):
        try:
            return Profile.objects.filter(pk=self.request.user.id).first()
        except Profile.DoesNotExist:
            return Profile.objects.none()

    def update_profile(request):
        if request.method == 'POST':
            # user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, _('Your profile was successfully updated!'))
                return redirect('directory:home')
            else:
                messages.error(request, _('Please correct the error below.'))
        else:
            # user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'profiles/profile.html', {
            'profile_form': profile_form
        })
