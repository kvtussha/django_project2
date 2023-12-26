import json
import logging

from django.shortcuts import render


def home_page(request):
    products_ = []
    with open('main_app/fixtures/main_app/products.json', encoding='utf-8') as f:
        products = json.load(f)
    for product_item in products:
        if len(products) < 12:
            products.append(product_item["fields"])
        else:
            break
    return render(request, 'main_app/home.html', {'products': products_})


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')
