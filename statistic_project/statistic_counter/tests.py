from rest_framework.test import APITestCase
from rest_framework import status
from .models import Statistic
from django.urls import reverse
from statistic_counter.serializers import SingleStatisticSerializer



class StatisticTests(APITestCase):
    
    def setUp(self):
        self.first_statistic = Statistic.objects.create(
            date="1233-3-11",
            views=321,
            clicks=4141,
            cost=52.99
        )
        self.long_date_range = {
            "date_from": "0001-1-1", 
            "date_to": "6666-12-12"
        }

    def test_view_list_not_empty(self):
        response = self.client.post(
            reverse('view_stat'),
            data=self.long_date_range
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_exists_all_fields(self):
        response = self.client.post(
            reverse('view_stat'),
            data=self.long_date_range
        )
        fields = ['date', 'views', 'clicks', 'cost', 'cpc', 'cpm']
        self.assertTrue(
            fields == 
            [field for field in response.json()[0].keys()]
        )
        
    def test_all_expected_values_after_create(self):
        input_value = {
            "date": "1233-3-11",
            "views": 11332,
            "clicks": 33,
            "cost": "3444.99",
        }
        response = self.client.post(
            reverse('create'),
            data=input_value
        )
        ser = SingleStatisticSerializer(input_value)
        internal_val = ser.to_internal_value(input_value)
        created = ser.create(internal_val)
        expected_value = dict(ser.to_representation(created))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_value)

    def test_all_fields_null_without_date(self):
        input_value = {
            "date": "4433-1-1",
        }
        expected_result = {
            "date": "4433-01-01",
            "views": None,
            "clicks": None,
            "cost": None,
            "cpc": None,
            "cpm": None
        }
        response = self.client.post(
            reverse('create'),
            data=input_value
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_result)

    def test_date_field_is_required(self):
        response = self.client.post(
            reverse('create'),
            data={}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(
            "This field is required." in response.json().get('date')
        )

    def test_invalid_date(self):
        input_value = {"date": "12-12-1999",}
        response = self.client.post(
            reverse('create'),
            data=input_value
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD." 
            in response.json().get('date')
        )

    def test_two_instanses_in_view_list(self):
        Statistic.objects.create(
            date="1444-11-11",
            views=111,
            clicks=222,
            cost=11.99
        )
        date_range = {
            "date_from": "1233-3-11", 
            "date_to": "1444-11-11"
        }
        response = self.client.post(
            reverse('view_stat'),
            data=date_range
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_all_statistic(self):
        response = self.client.delete(
            reverse('del_stat'),
            data={}
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Statistic.objects.all().exists())