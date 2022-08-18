from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Product



# Create your views here.


class  HomePage(ListView):
	model=Product
	template_name='index.html'


class MenuPage(ListView):
	
	model=Product
	template_name='menu.html'
	

class AboutPage(TemplateView):
	template_name='about.html'



class BookPage(TemplateView):
	template_name='book.html'
