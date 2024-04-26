from django.forms import ModelForm, Textarea, TextInput
from .models import OrderDetail


class NewOrderForm(ModelForm):

    class Meta:
        model = OrderDetail
        fields = ["address","phone",]
        labels = {
            
            "phone" : "Телефон для связи",
            "address" : "Адрес доставки",
        }
        widgets = {                           
            "phone" : TextInput(attrs={"class": "form-control"}),
            "address": Textarea(attrs={"cols": 40, "rows": 6, "class": "form-control", }),
        }
        
        



