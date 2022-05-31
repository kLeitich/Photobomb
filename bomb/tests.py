from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.location.save_location()
        self.location.delete()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)


    def test_update_method(self):
        self.location.save_location()
        self.location.update_location('Nairobi')
        location = Location.objects.all()
        self.assertTrue(len(location)>0)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name = 'food')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_update_method(self):
        self.category.save_category()
        self.category.update_category('travel')
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'bomet')
        self.location.save_location()
        self.category = Category(category_name = 'cars')
        self.category.save_category()
        self.image = Image(name = 'subaru',description = 'This is a picture of a car',
        location = self.location,category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # save
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    # delete
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)


# search by category
    def test_search_by_category(self):
        self.image.save_image()
        images = Image.search_by_category('Nature')
        self.assertTrue(len(images)>0)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
