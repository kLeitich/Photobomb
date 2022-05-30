from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.

class Location(models.Model):
    Location_name=models.CharField(max_length =30)

    def __str__(self):
        return self.Location_name

class Category(models.Model):
    category_name=models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

class Image(models.Model):
    image=models.ImageField(upload_to = 'index/')
    name= models.CharField(max_length =30)
    description= models.CharField(max_length =300)
    # location=models.ForeignKey('Location',on_delete=models.DO_NOTHING)
    # category=models.ForeignKey('Catergory',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.image

    def save_image(self):
        self.save(self)

    def filter_category(cls):
        image=cls.objects.filter(category)
