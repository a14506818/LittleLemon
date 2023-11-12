# myapp/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu  # Replace 'YourModel' with the actual name of your model

class YourViewTest(TestCase):

    def setUp(self):
        # Set up any necessary data for your tests
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Apple", Price=3, Inventory=20)

    def test_view_response(self):
        # Get the URL using reverse, assuming you have a URL pattern named 'your_view_name'
        url = reverse('menu')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON content of the response
        response_data = response.json()

        # Assert that the 'output_data' in the response matches the input_data
        self.assertEqual(response_data[0].get('Title'), "IceCream")
        self.assertEqual(response_data[1].get('Price'), 3)
