from django.urls import path

from main_app.views import (contacts, ProductDetailView, ProductsListView, PostListView,
                            PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, MessageListView,
                            MessageCreateView, MessageDetailView, MessageDeleteView, MessageUpdateView)

app_name = 'main_app'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/form/', PostCreateView.as_view(), name='post-form'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),

    path('messages/', MessageListView.as_view(), name='message-list'),
    path('message/form/', MessageCreateView.as_view(), name='message-form'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message-delete'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message-edit'),

]
