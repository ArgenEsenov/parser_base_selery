from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Категария'

    def __str__(self):
        return f'{self.name}'


class Ads(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=500)
    create_ad = models.DateTimeField('Дата создания', auto_now_add=True)



    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    ad = models.ForeignKey(Ads, verbose_name='Обьявления', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(verbose_name="Изображения", upload_to='ads_images', blank=True, null=True)
    image_url = models.URLField(blank=True, verbose_name='Ссылки Изображения', max_length=200, null=True)


    def __str__(self):
        return f"{self.image.name}"
