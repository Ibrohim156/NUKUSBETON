from django import forms
from . import models



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1',
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1',
                'placeholder': 'Ваш номер телефона'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1',
                'placeholder': 'Ваш email'
            }),
            'object_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1',
                'placeholder': 'Название объекта'
            }),
            'project_location': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1',
                'placeholder': 'Местоположение проекта'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-700 text-white rounded p-2 mt-1 resize-none h-24',
                'placeholder': 'Ваше сообщение'
            }),
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


