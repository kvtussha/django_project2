from django.urls import path

from main_app.views import catalog, home_page, contact_info

urlpatterns = [
    path('', home_page),
    path('catalog/', catalog),
    path('contact_info/', contact_info),
]
