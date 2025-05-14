from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('company/', views.company, name='company'),
    path('article/<slug:article_slug>/', views.article, name='article'),
    path('product/', views.brands, name='brands'),
    path('product/<slug:brand_slug>/', views.product_list, name='product_list'),
    path('product/<slug:brand_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),


]