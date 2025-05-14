from django.contrib import admin
from .models import Brand, Company, Product, Article, Contact, Feedback, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    prepopulated_fields = {'slug': ('brand_name',)}

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('city', 'history')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',  'price', 'pub_date')
    list_filter = ['brand']
    search_fields = ('product_name', 'description')
    prepopulated_fields = {'slug': ('product_name',)}    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'name', 'created_at')
    search_fields = ('email', 'name')