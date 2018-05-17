from django.db import models

# Create your models here.

class Seguridad(models.Model):
	"""docstring for Seguridad"""


	eMail = models.EmailField()
	password1 = models.CharField(max_length=16)
	password2 = models.CharField(max_length=16)

	def showData():
		print (eMail)
		pass

	def registrarUsuario(self,id,password1,password2):
		if (len(password1)>=8 and len(password1)<=16) and (password1==password2):
			
			return "Usuario válido"
		else: 
			return "Clave invalida"

	def IngresarUsuario(self,id, pass1):
		pass