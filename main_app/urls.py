from django.urls import path

from main_app.views import contacts, ProductDetailView, ProductsListView, PostListView, PostDetailView, PostCreateView, \
    PostDeleteView, PostUpdateView

app_name = 'main_app'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/form/', PostCreateView.as_view(), name='post-form'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),
]
