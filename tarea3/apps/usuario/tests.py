from django.test import TestCase
from apps.usuario.models import Seguridad 
# Create your tests here.
class TestSeguridad(TestCase):
	
	def test_Seguridad_registro(self):
		calc = Seguridad()
		self.assertEqual(None,calc.registrarUsuario("12-10199@usb.ve",12345678,12345678))

	def test_Seguridad_login(self):
		calc = Seguridad()
		self.assertEqual(None,calc.IngresarUsuario("12-10199@usb.ve",12345678))

	