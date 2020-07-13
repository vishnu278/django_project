from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'blog/home.html')

def products(request):
    return render(request,'blog/products.html')

def customers(request):
    return render(request,'blog/customer.html')
    