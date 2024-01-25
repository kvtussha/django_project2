from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.models import Product, Post, MailingMessage


class ProductsListView(ListView):
    model = Product
    template_name = 'main_app/product/product_list.html'
    context_object_name = 'products'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main_app/product/product_detail.html'
    context_object_name = 'product'


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image')
    context_object_name = 'post'
    success_url = reverse_lazy('main_app:post-list')

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.views_count = 0
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'main_app/post/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostListView(ListView):
    model = Post
    template_name = 'main_app/post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('main_app:post-detail')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main_app/post/post_confirm_delete.html'
    success_url = reverse_lazy('main_app:post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        return context


# -----------------------------------------------------------

class MessageListView(ListView):
    model = MailingMessage
    template_name = 'main_app/message/message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = MailingMessage
    template_name = 'main_app/message/message_detail.html'
    context_object_name = 'message'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.creation_date = timezone.now()
        self.object.save()
        return self.object


class MessageCreateView(CreateView):
    model = MailingMessage
    fields = ('subject', 'body', )
    context_object_name = 'message'
    template_name = 'main_app/message/message_form.html'
    success_url = reverse_lazy('main_app:message-list')


class MessageUpdateView(UpdateView):
    model = MailingMessage
    fields = ('subject', 'body',)
    success_url = reverse_lazy('main_app:message-detail')


class MessageDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'main_app/message/message_confirm_delete.html'
    success_url = reverse_lazy('main_app:message-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление уведомления'
        return context
