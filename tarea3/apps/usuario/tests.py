from django.test import TestCase
from apps.usuario.models import Seguridad 
# Create your tests here.
class TestSeguridad(TestCase):
	
	def test_registro_clave_menor_8(self):

		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","1234567","1234567"))

	def test_registro_clave_mayor_16(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","1234567maria++77","1234567maria++77"))

	def test_registro_min_tres_letras(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","12345678","12345678"))

	def test_registro_min_tres_letras_una_mayus(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","123mar45678","123mars45678"))

	def test_registro_password_una_mayus_un_dig_tres_letras(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","1232mAr45678","1232mAr45678"))

	def test_Seguridad_login(self):
		seg = Seguridad()
		self.assertEqual(None,seg.IngresarUsuario("12-10199@usb.ve",12345678))

	