from django.urls import path
from . import views

urlpatterns = [ path("", views.index, name = "secundario"),
		path("<str:nome>", views.saudacao,name="saudacao")]
