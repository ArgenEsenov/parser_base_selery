from .models import Category, Ads, Image
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CategorySerializers, AdsSerializers, ImageSerializers, ADSSerializer


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
        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageView(generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers