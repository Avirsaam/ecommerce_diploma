from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
  


from django import forms

class CustormerCreationForm(UserCreationForm):
    email = forms.EmailField(label='email')
    
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
    
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],              
        )
        
    

class UserRegistrationView(View):
    def get(self, request):
        form = CustormerCreationForm()
        context = {
            "page_title" : "Регистрация",
            "page_subtitle" : "нового пользователя",
            "form": form
        }        
        return render(request, "registration_app/user_registration_form_template.html", context)
    
    def post(self, request, *args, **kwargs):
        form = CustormerCreationForm(request.POST)               
        messages = []        
        if form.is_valid():
            form.save()
            customers, created = Group.objects.get_or_create(name='customers')
            user = User.objects.get(username=form.cleaned_data['username'])
            user.groups.add(customers.pk)
            user.save()
            messages.append('Пользователь успешно зарегистрирован')
            login(request, user)                                    
        context = {
            "page_title" : "Регистрация",
            "page_subtitle" : "нового пользователя",
            "form": form,
            "messages" : messages,
        }             
        return render(request, "registration_app/user_registration_form_template.html", context)
        
        
    
