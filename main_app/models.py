from django.db import models
from django.db.models import ForeignKey


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price_per_unit = models.IntegerField(verbose_name='цена за единицу')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price_per_unit}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', )


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', )


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='название')
    slug = models.TextField(verbose_name='slug')
    content = models.TextField(verbose_name='контент')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', null=True, blank=True)
    creation_date = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='статус публикации', null=True, blank=True)
    views_count = models.IntegerField(verbose_name='кол-во просмотров', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение блога'
        verbose_name_plural = 'сообщения блога'
        ordering = ('title', )


class ProductVersion(models.Model):
    version_name = models.CharField(max_length=200, verbose_name='version name')
    version_number = models.CharField(max_length=100, verbose_name='version number', default='1.0.0')
    is_active = models.BooleanField(default=True, verbose_name='статус версии', null=True, blank=True)
    product = ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='product')

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продукта'
        ordering = ('version_number', )
