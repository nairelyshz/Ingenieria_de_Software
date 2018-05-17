from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import SeguridadForm
from apps.usuario.forms import SeguridadForm2
from .models import Seguridad

# Create your views here.
class SeguridadView:

	def login(request):
		print (request)
		n = Seguridad()
		if request.method == "POST":
			form = SeguridadForm(request.POST)
			info = form.save(commit=False)
			print ("*****")
			print(n.registrarUsuario(info.eMail, info.password1, info.password2))
		else:
			form = SeguridadForm()
		return render(request, 'usuario/register.html', {'form': form})

	def ingresar(request):
		n = Seguridad()
		if request.method == "POST":
			form2 =  SeguridadForm2(request.POST)
			info2 = form2.save(commit=False)
			print(n.IngresarUsuario(info2.eMail,info2.password1))
		else:
			form2 = SeguridadForm2()
		return render(request, 'usuario/login.html', {'form2': form2})
		pass
	


