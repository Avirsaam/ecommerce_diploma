from django.contrib import admin
from .models import Image, ImageCategory

# Register your models here.
admin.site.register(ImageCategory)
admin.site.register(Image)
