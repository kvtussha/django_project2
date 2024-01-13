from django.urls import path

from main_app.views import home_page, contacts, item

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts),
    path('item/', item, name='item'),
]
