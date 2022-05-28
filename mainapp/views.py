from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request=request,template_name='mainapp/index.html')
def category(request):
    return render(request=request,template_name='mainapp/category.html')
class Contact(TemplateView):
    template_name = 'mainapp/contact.html'
class Listing(TemplateView):
    template_name = 'mainapp/listing.html'

def misol(request):
    return HttpResponse('<h1 stayle="color:red">salom</h1>')
