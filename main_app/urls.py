from django.urls import path

from main_app.views import contacts, ProductDetailView, ProductsListView

app_name = 'main_app'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='item'),
]
