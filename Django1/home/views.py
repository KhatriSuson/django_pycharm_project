from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request, 'price.html')


