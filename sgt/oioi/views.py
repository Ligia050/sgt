from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	return HttpResponse("Oi pessoal, criei agora essa nova aplicação que bonitinha ;) ")

def saudacao(request,nome):
	return render(request,'index.html')
