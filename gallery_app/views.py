from django.shortcuts import render
from django.views import View
from .models import Image, ImageCategory

# Create your views here.

class PortfolioView(View):  
  def get(self, request):
    context = {
      "page_title" : "Наше портфолио",
      "page_subtitle" : "Примеры наших работ, сделанных на заказ",
      "images" : Image.objects.filter(category=ImageCategory.objects.filter(name__icontains='работы на заказ').first()),
    }
    return render(request, 'gallery_app/gallery_template.html', context)