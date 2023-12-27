from django.shortcuts import render

from main_app.models import ProductModel


def home_page(request):
    products = ProductModel.objects.all()
    return render(request, 'main_app/home.html', {'products': products})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')
