from django import forms
from .models import Mineral

class MineralForm(forms.ModelForm):
    class Meta:
        model = Mineral
        fields = ['nom_min']
        widgets = {
            'nom_min': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del mineral'
            }),
        }
        labels = {
            'nom_min': 'Nombre del Mineral',
        }