from django.contrib import admin
from .models import Brand, Company, Product, Article,Feedback,Document, ProductionPhoto, ProductionVideo




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
    list_display = ('title', 'link')
    search_fields = ['title']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'object_name', 'project_location', 'message')
    search_fields = ('email', 'name')


@admin.register(ProductionPhoto)
class ProductionPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

@admin.register(ProductionVideo)
class ProductionVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video']






