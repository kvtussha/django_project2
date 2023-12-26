from django.urls import path

from main_app.views import home_page, contact_info

urlpatterns = [
    path('', home_page),
    path('contact_info/', contact_info),
]
