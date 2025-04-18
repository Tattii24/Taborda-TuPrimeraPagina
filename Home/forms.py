from django import forms

class CreacionZapatos(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    talla=forms.IntegerField(required=True)
    color=forms.CharField(max_length=30)
    fecha_creacion=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
