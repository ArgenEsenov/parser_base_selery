import logging
from .models import Category, Ads, Image
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CategorySerializers, AdsSerializers, ImageSerializers, ADSSerializer
from django.shortcuts import render, redirect
from .forms import *


class ADSView(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = ADSSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class AdsView(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        image_urls = request.POST.getlist('image_urls')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            for img in images:
                Image.objects.create(ad_id=obj.id, image=img)
        logging.error(serializer.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageView(generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers





def create(request):
    if request.method == 'POST':
        fm = AdsForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = AdsForm()
    return render(request, 'index.html', {'fm': fm})


def read(request):
    data = Ads.objects.all()
    return render(request, 'read.html', {'data': data})


def create(request):
    if request.method == 'POST':
        fm = AdsForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    else:
        fm = AdsForm()
        data = Ads.objects.all()
    return render(request, 'index.html', {'fm': fm, 'data': data})


def edit(request, id):
    dataget = Ads.objects.get(id=id)
    data = Ads.objects.all()
    fm = AdsForm(instance=dataget)
    if request.method == 'POST':
        fm = AdsForm(request.POST, instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    return render(request, 'index.html', {'fm': fm, 'data': data})


def delete(request, id):
    dataget = Ads.objects.get(id=id)
    dataget.delete()
    return redirect('create')
