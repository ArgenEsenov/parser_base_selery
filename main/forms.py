from django import forms

from .models import Ads, Image

class AdsForm(forms.ModelForm):

    class Meta:
        model = Ads
        fields = ('category', 'title', 'description', 'phone')

