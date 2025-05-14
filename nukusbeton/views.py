from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact, Article,Company,Brand, Category
from . import forms


def main(request):
    categories = Category.objects.all()
    return render(request, 'header/main.html', {
        'categories': categories,
    })


def category(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    context={
    'category': category,
    'categories': categories,
    }
    return render(request, 'header/category.html', context)

def contactus(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = forms.ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'header/contact.html', context)

def contact(request):
    form = Contact()
    return render(request, 'header/contact.html', {
        'form': form,
  })



def brands(request):
    brands = Brand.objects.all()
    return render(request, 'product/brands.html', {'brands': brands})

def product_list(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand)
    return render(request, 'product/product_list.html', {'products': products, 'brand': brand})

def product_detail(request, brand_slug, product_slug):
    product = get_object_or_404(Product, brand__slug=brand_slug, slug=product_slug)
    return render(request, 'product/product_detail.html', {'product': product})


    
def company(request):
    company = Company.objects.first()
    categories = Category.objects.all() 
    return render(request, 'header/company.html', {
        'company': company,
        'categories': categories,
    })

def article(request,articles_slug):
    article = get_object_or_404(Article, slug=articles_slug)
    return render(request, 'header/article.html', {'article': article})



