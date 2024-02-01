from django.contrib import admin

from main_app.models import Product, Category, Post, MailingLog, Message, Mailing, Client, ProductVersion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'category', )
    list_filter = ('name', 'description', 'category', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'comment', )


@admin.register(Mailing)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'frequency', 'status', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', )


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('attempt_datetime', 'attempt_status', 'server_response')


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'current_version')
