from django.shortcuts import render
from django.urls import reverse

from main_app.models import ProductModel


def home_page(request):
    products = ProductModel.objects.all()
    product_url = reverse('item')
    return render(request, 'main_app/home.html',
                  {'products': products, 'product_url': product_url})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')


def item(request):
    return render(request, 'main_app/item.html')
