from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from main_app.models import Product, Category, Post, Message, ProductVersion


class ProductCreateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price_per_unit')

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ["казино", "криптовалюта", "крипто", "биржа", "дешево", "бесплатно",
                           "мошенничество", "полиция", "радар"]

        for word in forbidden_words:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово '{word}' запрещено использовать в названии продукта. ")

        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ["казино", "криптовалюта", "крипто", "биржа", "дешево", "бесплатно",
                           "мошенничество", "полиция", "радар"]

        for word in forbidden_words:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' запрещено использовать в описании продукта.")

        return description


class ProductUpdateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price_per_unit')


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class MessageCreateForm(ModelForm):
    sent = forms.BooleanField(initial=False, required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Message
        fields = ('subject', 'body', 'sent')


class MessageUpdateForm(ModelForm):
    sent = forms.BooleanField(initial=False, required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Message
        fields = ('subject', 'body', 'sent')


class VersionCreateForm(ModelForm):
    class Meta:
        model = ProductVersion
        fields = ('version_name', 'version_number', 'current_version')


class VersionUpdateForm(ModelForm):
    class Meta:
        model = ProductVersion
        fields = ('version_name', 'version_number', 'current_version')

