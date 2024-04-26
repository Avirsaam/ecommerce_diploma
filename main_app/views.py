from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings
import os


class IndexPageVies(View):
    def get(self, request):
        static_dir = 'static/images/index_slideshow1/'        
        context = {
            "images": [os.path.join(static_dir, fn) for fn in os.listdir(static_dir)]
            }
        print(context)
        return render(request, "main_app/index.html", context)
    
class CustomKnittingView(View):
    def get(self, request):
        context = {
            "page_title" : "Вязаные вещи на заказ",
            "page_subtitle" : "Связано с любовью"    
        }
        return render(request, "main_app/custom_knitting.html", context)

class AboutView(View):
    def get(self, request):
        context = {
            "page_title" : "О нашей компании",            
        }
        return render(request, "main_app/about.html", context)


class ContactsPageView(View):
    def get(self, request):
        context = {
            "page_title" : "Контактные",
            "page_subtitle" : "Наш адрес и телефон"
        }
        return render(request, "main_app/contacts.html", context)
    
class PaymentAndDeliveryView(View):
    def get(self, request):
        context = {
            "page_title" : "Информация об оплате",            
        }
        return render(request, "main_app/payment_and_delivery.html", context)

