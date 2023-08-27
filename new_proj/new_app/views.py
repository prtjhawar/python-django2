from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def  instagram(request):
    return render(request,'instagram.html')

def  product(request):
    return render(request,'product.html')

def  preeti(request):
    return render(request,'preeti.html')

def task(request):
    return render(request,'task.html')

