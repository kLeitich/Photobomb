from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.model):
    image=models.ImageField(upload_to = 'index/')
    name= models.CharField(max_length =30)
    description= models.CharField(max_length =300)
    location=models.ForeignKey('Location')
    category=models.ForeignKey('Catergory')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save(self)

    def filter_category(cls):
        image=cls.objects.filter(category)
