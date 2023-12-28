from django.urls import path

from main_app.views import home_page, contact, item

urlpatterns = [
    path('', home_page),
    path('contact/', contact),
    path('item/', item),
]
