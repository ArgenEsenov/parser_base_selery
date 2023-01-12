from django.contrib import admin
from .models import Category, Ads, Image


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Image)
