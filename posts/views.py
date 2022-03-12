from django.shortcuts import render
from .models import Post, Product, Category


def index(request):
	return render (request, "posts/index.html")

def women(request):
	return render (request, "posts/women.html")

def shoes(request):
	return render (request, "posts/shoes.html")



def products_men(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'products': products,
		'categories': categories
	}
	return render (request, "posts/jackets-coats-men.html", context)


def contact(request):
	return render (request, "posts/contact.html")

