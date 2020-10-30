from django import forms
from .models import Correo, Prestamo, Libro



class PrestamoMultipleForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField(
        queryset = None, 
        required = True,
        widget= forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamo
        fields = ('lector',)

    def __init__(self, *args, **kwargs):
        
        super(PrestamoMultipleForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()




class PrestamoForm(forms.ModelForm):
    
    class Meta:
        model = Prestamo
        fields = ("lector","libro",)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ['name', 'email', 'message', 'telefono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        
        self.fields['name'].widget.attrs={'class': 'form-control', 'placeholder':'Nombre'}
        self.fields['email'].widget.attrs={'class': 'form-control', 'placeholder':'Correo'}
        self.fields['telefono'].widget.attrs={'class': 'form-control', 'placeholder':'Télefono'}
        self.fields['message'].widget.attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows':5, 'required':True}