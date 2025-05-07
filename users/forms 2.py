from django import forms 
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(disabled=True)
    username = forms.CharField(disabled=True)  # ✅ ADD THIS LINE

    class Meta:
        model = UserProfile
        fields = ['street_number', 'zipcode', 'city', 'country', 'profile_pic', 'bio']
        # ^ Don't include 'username' here since it's from the User model

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['username'].initial = user.username  # ✅ This will now work!
