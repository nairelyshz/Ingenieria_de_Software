from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import SeguridadForm
from .models import Seguridad
import unittest
# Create your views here.
class SeguridadView:

	def login(request):
		print (request)
		n = Seguridad()
		if request.method == "POST":
			form = SeguridadForm(request.POST)
			n.registrarUsuario("id","12345678","12345678");
		else:
			form = SeguridadForm()
		return render(request, 'usuario/register.html', {'form': form})


	


