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


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Letter subject')
    body = models.TextField(verbose_name='Body of the letter')
    sent = models.BooleanField(verbose_name='Отправка', default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылки'


class Mailing(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Once a day'),
        ('weekly', 'Once a week'),
        ('monthly', 'Once a month'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('created', 'Created'),
        ('started', 'Started'),
    ]

    mailing = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='messages',
                                verbose_name='Mailing message')
    mailing_time = models.TimeField(verbose_name='Mailing time')
    frequency = models.CharField(max_length=7, choices=FREQUENCY_CHOICES, verbose_name='Frequency')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Mailing status')

    def __str__(self):
        return f'{self.get_frequency_display()} Mailing at {self.mailing_time} - {self.get_status_display()}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):
    mailing = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='logs', verbose_name='Mailing time')
    attempt_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Date and time of last attempt')
    attempt_status = models.CharField(max_length=15, verbose_name='Attempt status')
    server_response = models.TextField(blank=True, null=True, verbose_name='Mail server response, if any')

    def __str__(self):
        return f'{self.attempt_datetime} - {self.attempt_status}'

    class Meta:
        verbose_name = 'Журнал рассылки'
        verbose_name_plural = 'Журналы рассылки'


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='client name')
    contact_email = models.EmailField()
    comment = models.TextField(verbose_name='comment', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='product id')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='post id')
    mailing = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True, related_name='mailings',
                                verbose_name='Mailing time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('name', )


class ProductVersion(models.Model):
    version_name = models.CharField(max_length=200, verbose_name='version name')
    version_number = models.CharField(max_length=100, verbose_name='version number', default='1.0.0')
    current_version = models.CharField(max_length=100, verbose_name='version number', default='1.0.0')
    product = ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='product')

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продукта'
        ordering = ('version_number', )
