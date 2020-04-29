from django.db import models

# Create your models here.
class Image(models.Model):
    comment = models.CharField(max_length=200)
    dest = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name