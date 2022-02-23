from django.shortcuts import render
from .models import Post


def index(request):
	return render (request, "posts/index.html")

def woman(request):
	return render (request, "posts/woman.html")

def shoes(request):
	return render (request, "posts/shoes.html")