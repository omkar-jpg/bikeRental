from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'street_number', 'zipcode', 'city', 'country', 'profile_pic', 'bio']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
        if 'username' in self.fields:
            self.fields['username'].required = False

    def clean(self):
        cleaned_data = super().clean()
        if 'username' in self.fields and self.fields['username'].widget.attrs.get('disabled'):
            cleaned_data.pop('username', None)
        return cleaned_data