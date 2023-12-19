from django.contrib import admin

from main_app.models import ProductModel, CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'category', )
    list_filter = ('name', 'description', 'category', )