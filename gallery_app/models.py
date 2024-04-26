from django.db import models


class ImageCategory(models.Model):
  name = models.CharField('Категория', max_length=50)
  
  def __str__(self):
      return self.name  
  
  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категория изображений'
  
class Image(models.Model):
  name = models.CharField('Название', max_length=50)
  description = models.TextField('Описание')
  image = models.ImageField('Изображение', upload_to='images/')
  category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
  
  def __str__(self):
    return str(self.name)
  
  class Meta:
    verbose_name = 'Галерея'
    verbose_name_plural = 'Галерея'
