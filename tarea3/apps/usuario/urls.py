from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^registrar', views.SeguridadView.login,name="registrar"),
	#url(r'^signIng', views.Seguridad.post_new,name="signIn"),

]