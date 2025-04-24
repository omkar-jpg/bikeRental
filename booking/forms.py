from django import forms
from .models import Booking  # Import the Booking model

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Specify the model the form is based on
        fields = ['start_date', 'end_date', 'quantity']  # Fields to be included in the form
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),  # Use date input widget for start date
            'end_date': forms.DateInput(attrs={'type': 'date'}),    # Use date input widget for end date
        }
