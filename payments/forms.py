from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_id', 'amount_paid']
        widgets = {
            'payment_id': forms.TextInput(attrs={'placeholder': 'Enter UPI/Phone number'}),
            'amount_paid': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
        }