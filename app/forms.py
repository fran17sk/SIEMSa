# forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import Mineral,User,Organismo
from .models_catastro import Contratos


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
class ContratosForm(forms.ModelForm):
    fecha_ini = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Contratos
        fields = [
             'id_concesionario', 'paga_canon','mineral_explotacion',
            #'explotacion', 'exploracion', 'iia',
            'activo', 'fecha_ini', 'fecha_fin', #'pago_regalias'
        ]
        widgets = {
            'id_concesionario': forms.TextInput(attrs={'class': 'form-control'}),
            'paga_canon': forms.TextInput(attrs={'class': 'form-control'}),
            ##'explotacion': forms.TextInput(attrs={'class': 'form-control'}),
            'mineral_explotacion': forms.TextInput(attrs={'class': 'form-control'}),
            ##'exploracion': forms.TextInput(attrs={'class': 'form-control'}),
            ##'iia': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.TextInput(attrs={'class': 'form-control'}),
            ##'pago_regalias': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

class UserCreateForm(forms.ModelForm):
    organismos = forms.ModelMultipleChoiceField(
        queryset=Organismo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff', 'password']