from django.test import TestCase
from apps.usuario.models import Seguridad 
# Create your tests here.
class TestSeguridad(TestCase):
	
	def test_registrar_primer_argumento(self):
		seg = Seguridad()
		self.assertRaises(TypeError, registrarUsuario, Decimal(2), "hola_1", "hola_2")
		self.assertRaises(TypeError, registrarUsuario, [], "hola_1", "hola_2")
		regisro = seg.registrarUsuario("hola_1", "hola_2", "hola_3") 
	
	def test_registrar_segundo_argumento(self):
		seg = Seguridad()
		self.assertRaises(TypeError, registrarUsuario, Decimal(1), "hola")
		self.assertRaises(TypeError, registrarUsuario, Decimal(1), [])
		registro = seg.registrarUsuario("id", "pass1","pass2")


	def test_registro_clave_menor_8(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","1234567","1234567"))

	def test_registro_clave_mayor_16(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","1234567maria++77","1234567maria++77"))

	def test_registro_min_tres_letras(self):
		seg = Seguridad()
		self.assertRaises(TypeError,registrarUsuario,"12-10199@gmail.com","12345678","12345678")
		regisro = registrarUsuario("12-10199@gmail.com","1234mns5678","12345678")

	def test_registro_min_tres_letras_una_mayus(self):
		seg = Seguridad()
		self.assertEqual("Clave invalida",seg.registrarUsuario("12-10199@gmail.com","123mar45678","123mars45678"))

	def test_registro_password_una_mayus_un_dig_tres_letras(self):
		seg = Seguridad()
		self.assertEqual("Usuario válido",seg.registrarUsuario("12-10199@gmail.com","1232mAr45678","1232mAr45678"))

	
	

	