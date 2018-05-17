from django.db import models

# Create your models here.

class Seguridad(models.Model):
	"""docstring for Seguridad"""
	users = {}

	eMail = models.EmailField()
	password1 = models.CharField(max_length=16)
	password2 = models.CharField(max_length=16)



	def registrarUsuario(self,id,password1,password2):
		#Primer argumento debe ser de tipo string
		if not isinstance(id, str):
			raise TypeError ("ERROR: Primer argumento debe ser de tipo str")
    #Segundo argumento debe ser de tipo string
		if not isinstance(password1, str):
			raise TypeError ("ERROR: Segundo argumento debe ser de tipo lista")
    #Tercer argumento debe ser de tipo string
		if not isinstance(password2, str):
			raise TypeError ("ERROR: Tercer argumento debe ser de tipo lista")
		valido = False;
		contadorArroba = 0;
		contadorPunto = 0;
		for i in id:
			if(i == '@'):
				contadorArroba += 1
				valido = True
			if(contadorArroba != 1 and contadorPunto < 1):
				valido = False
			if(i == '.'):
				contadorPunto += 1
		if(valido):
			if (len(password1)>=8 and len(password1)<=16) and (password1==password2):
				self.users.setdefault(id,password1)
				return "Usuario válido"
			else: 
				return "Clave invalida"
		else:
   			return "direccion erronea"
		

	def IngresarUsuario(self,id, pass1):
		if self.users.get(id)!=None:
			if self.users.get(id)==pass1 :
				return "Usuario aceptado"
			else:
				return "Clave inválida"
		else:
			return "Usuario inválido"