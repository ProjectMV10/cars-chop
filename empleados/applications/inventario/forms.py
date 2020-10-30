from django import forms
from .models import *


class CarForm(forms.Form):

    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'input-group-field',
            }
        )
    )
    #
    def clean_count(self):
        cantidad = self.cleaned_data['cantidad']
        if count < 1:
            raise forms.ValidationError('Ingrese una cantidad mayor a cero')

        return cantidad