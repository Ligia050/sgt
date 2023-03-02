from django.urls import path
from . import views

urlpatterns = [ 
		#path("<str:nome>", views.greet,name="greet"),
		path("<str:nome>", views.tia_do_zap,name="tia do zap")
		]
