from django.urls import path

from main_app.views import home_page, contacts, item

app_name = 'main_app'

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts),
    path('item/<int:pk>/', item, name='item'),
]
