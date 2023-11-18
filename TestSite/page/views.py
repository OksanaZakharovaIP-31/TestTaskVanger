from django.shortcuts import render
from .models import slider
from easy_thumbnails.files import get_thumbnailer
from django.http import HttpResponse


# Create your views here.


def index(request):
    photo_slider_1 = slider.objects.all()
    return render(request, 'page/index.html', context={'photo_slider_1': photo_slider_1})
