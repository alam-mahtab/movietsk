from rest_framework.test import APITestCase
from django.urls import reverse

class Testsetup(APITestCase):

    def setUp(self):
        self.list_url = reverse('movie_list')

        self.user_data = {
            "Name": "Baghban",
        "Description": "The film narrates the story of an elderly couple, Raj (Amitabh Bachchan) and Pooja (Hema Malini)",
        "Date_Of_Release": "2021-05-30"
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
