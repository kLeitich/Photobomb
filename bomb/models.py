from django.db import models

# Create your models here.
class Image(models.model):
    image=models.ImageField(upload_to = 'index/')
    name= models.CharField(max_length =30)
    description= models.CharField(max_length =300)
    location=models.ForeignKey('Location')
    category=models.ForeignKey('Catergory')