from django.test import TestCase
from .models import Location,Tag
import datetime as dt

# Test case for locations
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

# Test case for categories
class TagTestClass(TestCase):
    def setUp(self):
        self.tag = Tag(tag='vacay')

    def test_tag_instance(self):
        self.assertTrue(isinstance(self.tag, Tag))

    def test_save_tag_method(self):
        self.tag.save_tag()
        tag_object = Tag.objects.all()
        self.assertTrue(len(tag_object) > 0)

    def test_delete_tag_method(self):
        self.tag.save_tag()
        tag_object = Tag.objects.all()
        self.tag.delete_tag()
        tag_object = Tag.objects.all()
        self.assertTrue(len(tag_object) == 0)