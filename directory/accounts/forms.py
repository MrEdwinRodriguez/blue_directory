from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User, Profile


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = "Email Address"
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('chapters_pledged', 'year_pledged', 'current_chapter', 'major', 'year_graduated', 'current_position', 'linkedin', 'phone_number', 'other_info', 'business')


