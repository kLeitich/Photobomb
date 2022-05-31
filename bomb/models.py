from unicodedata import category
from django.db import models

# Create your models here.

class Location(models.Model):
    location_name=models.CharField(max_length =30)

    def __str__(self):
        return self.Location_name

    def save_location(self):
        self.save(self)

    def delete_location(self):
        self.delete(self)
    
    @classmethod
    def update_location(cls,location_name):
        cls.objects.filter(location_name=location_name).update(location_name=location_name)
    
    @classmethod
    def filter_by_location(cls,loc):
        images = cls.objects.filter(loc__location_name__icontains=loc)
        return images

class Category(models.Model):
    category_name=models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save(self)

    def delete_category(self):
        self.delete(self)
    
    @classmethod
    def update_category(cls,category_name):
        cls.objects.filter(category_name=category_name).update(category_name=category_name)

    

class Image(models.Model):
    image=models.ImageField(upload_to = 'category/')
    name= models.CharField(max_length =30)
    description= models.CharField(max_length =300)
    location=models.ForeignKey('Location',on_delete=models.DO_NOTHING,null=True)
    category=models.ForeignKey('Category',on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save(self)
    def delete_image(self):
        self.delete(self)
    @classmethod
    def update_image(self,cls,id,image):
        images=cls.objects.filter(id=id).update(image=image)
        return images
    

    @classmethod
    def get_all_images(cls):
        images=cls.objects.all()
        return images
    @classmethod
    def get_image_id(cls,id):
        cls.objects.filter(id=id)

    @classmethod
    def update_image(cls,id,image):
        cls.objects.filter(id=id).update(image=image)
    @classmethod
    def search_by_category(cls,search_term):
        images=cls.objects.filter(category__icontains=search_term)
        return images
    @classmethod
    def filter_by_category(cls,category_id):
        images = cls.objects.filter(category_id=category_id)
        return images