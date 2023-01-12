from django.shortcuts import render
from .models import *
# Create your views here.

def category(request):
    category = Category.objects.all()
    context = {'categories':category}
    return render(request, "store/category.html", context)

def home(request):
    return render(request, "store/index.html")
