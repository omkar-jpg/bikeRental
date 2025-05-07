from django import forms 
from .models import BikeRating

class BikeRatingForm(forms.ModelForm):
    class Meta:
        model = BikeRating
        fields = ['rating', 'comment']

    rating = forms.ChoiceField(choices=[(i, f'{i} Stars') for i in range(1, 6)], required=True)