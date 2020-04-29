from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class PortFolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paragraph_about = models.TextField(default=None)
    showcase_content = models.CharField(max_length=100, default=None)
    showcase_image= models.ImageField(upload_to="pics", default=None)
    about_image= models.ImageField(upload_to="pics", default=None)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, default=None)
    dest = models.CharField(max_length=100, default=None)
    img = models.ImageField(upload_to="pics", default=None)


class ServiceBox(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='servicebox', null=True)
    providing_field= models.CharField(max_length=200, default=None)
    sub_field=models.CharField(max_length=100, default=None)
