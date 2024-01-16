from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main_app.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'main_app/home.html'
    context_object_name = 'products'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main_app/item.html'
    context_object_name = 'product'
