from django import forms
from . import models



class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название продукта'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержимое'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата создания'}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


