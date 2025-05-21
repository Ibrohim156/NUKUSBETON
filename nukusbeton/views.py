from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Article,Company,Brand
from . import forms
from django.templatetags.static import static

def documents_view(request):
    context = {
        'document1_url': static('docs/contract1.pdf'),
        'document2_url': static('docs/contract2.pdf'),
    }
    return render(request, 'documents.html', context)


def main(request):
    return render(request, 'header/main.html', {
    })



def contactus(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = forms.FeedbackForm()

    context = {
        'form': form,
    }
    return render(request, 'header/contact.html', context)




def brands(request):
    brands = Brand.objects.all()
    return render(request, 'products/brands.html', {'brands': brands})

def product_list(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    products = Product.objects.filter(brand=brand)
    return render(request, 'products/product_list.html', {'brand': brand, 'products': products})

def product_detail(request, brand_id, product_id):
    product = get_object_or_404(Product, pk=product_id, brand__id=brand_id)
    return render(request, 'products/product_detail.html', {'product': product})
    
def company(request):
    company = Company.objects.first()
    return render(request, 'header/company.html', {
        'company': company,
    })


# def article(request, articles_id):
#     article = get_object_or_404(Article, id=articles_id)
#     return render(request, 'header/article.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'header/article.html', {'articles': articles})

def documents(request):
    context = {
        'document1_url': static('docs/contract1.pdf'),
        'document2_url': static('docs/contract2.pdf'),
        'document3_url': static('docs/contract3.pdf'),
    }
    return render(request, 'products/documents.html', context)

def media(request):
    return render(request, 'products/media.html', {
        'media': static('media/'),
    })
