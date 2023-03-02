from django.shortcuts import render

from django.http import HttpResponse



def index(request):
	return HttpResponse("Oi pessoal, criei agora essa nova aplicação que bonitinha ;) ")

def saudacao(request,nome):
	return render(request,'index.html')

def greet(request,nome):
	return render(request,'greet.html',{'nome':nome})

def tia_do_zap(request,nome):
	return render(request,'tia_do_zap.html',{'nome':nome,'dia':False})