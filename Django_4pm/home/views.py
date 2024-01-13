from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    views = {}
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()

    return render(request, 'index.html',views)


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        na = request.POST['name']
        em = request.POST['email']
        sub = request.POST['subject']
        mes = request.POST['message']
        data = Contact.objects.create(
            name = na,
            email = em,
            subject = sub,
            message = mes
        )
        data.save()
    return render(request, 'contact.html')

def price(request):
    views = {}
    views['prices'] = Price.objects.all()
    return render(request, 'price.html',views)

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'elements.html')


def blog(request):
    return render(request,'blog-home.html')

def blog_home(request):
    views = {}
    views['blogs'] = Blog.objects.all()
    return render(request, 'blog-home.html',views)


def blog_single(request, id):
    views = {}
    views['blog_details'] = Blog.objects.filter(id=id)
    return render(request,'blog-single.html',views)


def element(request, id):
    views = {}
    views['element'] = Elements.objects.filter(id=id)
    return render(request, 'elements.html', views)







