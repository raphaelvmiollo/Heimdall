# -*- coding: utf-8 -*- 
from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
	size_search = 3
	msg = ""
	if request.GET:
		busca = request.GET['buscar']		
		sites = site.objects.filter(nome__contains=busca)
		if len(sites) != 0:
			return render(request, 'index.html', {'sites': sites, 'msg': msg})
		msg = u"A busca não retornou nenhum resultado"
	
	sites = site.objects.all()
	return render(request, 'index.html', {'sites': sites, 'msg': msg})


def cadastraSite(request):
	pass