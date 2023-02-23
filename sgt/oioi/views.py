from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	return HttpResponse("Oi pessoal, criei agora essa nova aplicação que bonitinha ;) ")
