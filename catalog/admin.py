from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "product")

