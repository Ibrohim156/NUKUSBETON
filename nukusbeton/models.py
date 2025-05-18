from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    brand_name = models.CharField(max_length=250, verbose_name="Каталог")

    def __str__(self):
        return self.brand_name


    
    class Meta:
        verbose_name_plural = "Каталог"



class Company(models.Model):
    city = models.TextField(verbose_name="Наш город")
    history = models.TextField(verbose_name="История компании")
    catalog_xbik = models.FileField(upload_to='catalogs/', verbose_name="Каталог ЖБИ")
    typical_contract = models.FileField(upload_to='contracts/', verbose_name="Типовой договор")
    concrete_contract = models.FileField(upload_to='contracts/', verbose_name="Договор на поставку товарного бетона")
    xbik_contract = models.FileField(upload_to='contracts/', verbose_name="Договор на поставку ЖБИ")

    def __str__(self):
        return "О компании"
    
    class Meta:
        verbose_name_plural = "О компании"



class Product(models.Model):
    product_name= models.CharField(max_length=250,verbose_name="Название продукта")
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Каталог")
    description= models.TextField(verbose_name="Описание")
    main_image= models.ImageField(upload_to='products/', verbose_name="Главное изображение")
    image2= models.ImageField(upload_to='products/',verbose_name="Дополнительное изображение 1",
                              blank=True, null=True)
    image3= models.ImageField(upload_to='products/',verbose_name="Дополнительное изображение 2",
                              blank=True, null=True)
    image4= models.ImageField(upload_to='products/',verbose_name="Дополнительное изображение 3",
                                blank=True, null=True)
    pub_date= models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")
    price= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.product_name

 

    class Meta:
        verbose_name_plural = "Продукт"

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to='articles/', verbose_name="Изображение статьи", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self):
        return self.title
    
   

    class Meta:
        verbose_name_plural = "Статьи"


class Contact(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    map_photo = models.ImageField(upload_to='contacts/maps/', blank=True, null=True, verbose_name="Фото c карты")
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name_plural = "Контакты"

class Feedback(models.Model):
    name = models.CharField(max_length=55, verbose_name="Ваше имя")
    email = models.EmailField(verbose_name="Ваш адрес электронной почты")
    phone = models.CharField(max_length=20, verbose_name="Ваш номер телефона")
    message = models.TextField(verbose_name="Сообщение")
    object_name = models.CharField(max_length=255, verbose_name="Объект", blank=True, null=True)
    project_location = models.CharField(max_length=255, verbose_name="Местоположение проекта", blank=True, null=True)
    

    def __str__(self):
        return f"Сообщение от {self.email}"

    class Meta:
        verbose_name_plural = "Обратная связь"




