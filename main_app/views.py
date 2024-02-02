from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.forms import ProductCreateForm, ProductUpdateForm, PostCreateForm, PostUpdateForm, VersionCreateForm, VersionUpdateForm
from main_app.models import Product, Post, ProductVersion


class ProductsListView(ListView):
    model = Product
    template_name = 'main_app/product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main_app/product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        try:
            version = ProductVersion.objects.get(product=product)
        except ProductVersion.DoesNotExist:
            version = None

        context['version'] = version
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('main_app:product-list')
    template_name = 'main_app/product/product_form.html'

    def form_valid(self, form):
        form.instance.views_count = 0
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'main_app/product/product_form.html'

    def get_success_url(self):
        return reverse('main_app:product-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.last_modified_date = timezone.now()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main_app/product/product_confirm_delete.html'
    success_url = reverse_lazy('main_app:product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        return context


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'main_app/contacts.html')


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


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('main_app:post-list')
    template_name = 'main_app/post/post_form.html'

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.views_count = 0
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'main_app/post/post_form.html'

    def get_success_url(self):
        return reverse('main_app:post-detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main_app/post/post_confirm_delete.html'
    success_url = reverse_lazy('main_app:post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        return context


class VersionDetailView(DetailView):
    model = ProductVersion
    template_name = 'main_app/version/version_detail.html'
    context_object_name = 'version'

    def get_object(self, queryset=None):
        version_id = self.kwargs.get('version_id')
        return ProductVersion.objects.get(id=version_id)


class VersionCreateView(CreateView):
    model = ProductVersion
    form_class = VersionCreateForm
    template_name = 'main_app/version/version_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main_app:product-detail', kwargs={'pk': self.kwargs.get('pk')})


class VersionUpdateView(UpdateView):
    model = ProductVersion
    template_name = 'main_app/version/version_form.html'
    form_class = VersionUpdateForm

    def get_success_url(self):
        return reverse('main_app:version-detail', kwargs={'version_id': self.object.pk})
