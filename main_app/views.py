from django.shortcuts import render


def home_page(request):
    return render(request, 'main_app/home_page.html')


def catalog(request):
    return render(request, 'main_app/catalog.html')


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contact_info.html')
