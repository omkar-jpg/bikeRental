# loginsignup/adapter.py
# loginsignup/adapter.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        # Always allow signup
        return True

    def pre_social_login(self, request, sociallogin):
        # Skipping the confirmation page and redirecting to the account chooser
        if sociallogin.account.provider == 'google':
            # Redirect to the provider's login URL (this skips the confirmation step)
            return redirect(sociallogin.account.get_provider().get_login_url(request))
