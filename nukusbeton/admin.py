from django.contrib import admin
from .models import Brand, Company, Product, Article, Contact, Feedback




@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('city', 'history')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',  'price', 'pub_date')
    list_filter = ['brand']
    search_fields = ('product_name', 'description')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'object_name', 'project_location', 'message')
    search_fields = ('email', 'name')