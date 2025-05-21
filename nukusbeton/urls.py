from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contactus, name='contact'),
    path('company/', views.company, name='company'),
    # path('article/<int:articles_id>/', views.article, name='article'),
    path('article/', views.article_list, name='article_list'),
    path('product/', views.brands, name='brands'),  
    path('product/<int:brand_id>/', views.product_list, name='product_list'),  
    path('product/<int:brand_id>/<int:product_id>/', views.product_detail, name='product_detail'),
    path('documents/', views.documents, name='documents'),
    path('media/', views.media, name='media'),
]
