from django import forms
from .models import Seguridad

class SeguridadForm(forms.ModelForm):
	password1 = forms.CharField(required=True, min_length=8, max_length=16)
	class Meta:
		model = Seguridad
		fields = ['eMail','password1','password2']
		labels ={'eMail':'Correo',
				  'password1': 'Contraseña',
				  'password2': 'Confirmar contraseña'}
		
			
