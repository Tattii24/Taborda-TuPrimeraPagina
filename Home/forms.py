from django import forms
from .models import Zapato
from django.core.validators import FileExtensionValidator

class CreacionZapatos(forms.ModelForm):  # Cambia a ModelForm
    class Meta:
        model = Zapato
        fields = ['marca', 'modelo', 'talla', 'color', 'fecha_creacion', 'imagen']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'talla': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = False
        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })
    
    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen and imagen.size > 5 * 1024 * 1024:  # 5MB máximo
            raise forms.ValidationError("El tamaño máximo de la imagen es de 5MB")
        return imagen