from django.test import TestCase
from django.urls import reverse

import json

from .models import Record
from rest_framework.test import APITestCase

class TestKickBoxAuthorizationWebhook(APITestCase):

    def test_should_save_the_speed_as_json(self):
        url = reverse('backend:momentary_speed')
        speed = {"x": 1.1, "y": 1.3, "z": 2.3}

        resp = self.client.post(url, json.dumps(speed), content_type='application/json')

        self.assertEqual(resp.status_code, 200)
        record = Record.objects.first()
        self.assertEquals(record.json_data, json.dumps(speed))
            
