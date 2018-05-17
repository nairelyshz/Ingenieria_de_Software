from django.conf.urls import url
from apps.usuario import views

urlpatterns = [
	url(r'^registrar', views.SeguridadView.login,name="registrar"),
	url(r'^ingresar', views.SeguridadView.ingresar,name="ingresar"),

]