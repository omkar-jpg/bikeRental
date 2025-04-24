# from django.shortcuts import render
# from .forms import UserProfileForm
# from django.contrib.auth.decorators import login_required

# #@login_reqired
# def profile_view(request):
#     user = request.user
#     profile = user.userprofile

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request)
#         if form.is_valid():
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.save()

#             form.save()
#             return render(request, 'booking.html')

            

