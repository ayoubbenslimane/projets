from django.shortcuts import render

# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse
def home(request):
	
	text = """<h1>Bienvenue a wlad lkhab !</h1>
	<p>ha wahed zob fi zok  ça tue des mouettes en plein vol !</p>"""
	return HttpResponse(text)
    
    
    
