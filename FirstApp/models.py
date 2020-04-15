from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=200)
    dest = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
