from rest_framework import serializers
from .models import (Category,
                     Ads,
                     Image)

class ADSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class AdsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = ('category', 'user', 'title', 'price', 'description', 'phone', 'create_ad')

    def create(self, validated_data):
        category = validated_data.pop('category')
        ads = Ads.objects.create(category=category, **validated_data)
        return ads


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',  'ad')