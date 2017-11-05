from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase

import json

from .models import Record, Dance, DanceRecord
from .serializers import DanceSerializer

class TestAPI(APITestCase):

    def test_should_save_the_speed_as_json(self):
        url = reverse('backend:momentary_speed')
        speed = {"x": 1.1, "y": 1.3, "z": 2.3}

        resp = self.client.post(url, json.dumps(speed), content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        record = Record.objects.first()
        self.assertEquals(record.json_data, speed)
   
    def test_should_create_dance(self):
        url = reverse('backend:dance')
        
        resp = self.client.post(url, json.dumps({'name': 'k-pop'}), content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        dance = Dance.objects.first()
        self.assertEquals(dance.name, 'k-pop')

    def test_should_add_record_to_dance(self):
        url = reverse('backend:record')
        dance = Dance(name='test')
        dance.save()
        record = {'x': 1.3, 'y': 4.5, 'z': -0.1, 'dance': dance.pk, 'time':2983479}

        resp = self.client.post(url, json.dumps(record), content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        dance_record = DanceRecord.objects.first()
        self.assertEquals(dance_record.x_speed, record.get('x'))
        self.assertEquals(dance_record.y_speed, record.get('y'))
        self.assertEquals(dance_record.z_speed, record.get('z'))
        self.assertEquals(dance_record.dance.pk, dance.pk)
        self.assertEquals(dance_record.time, record.get('time'))
 
    def test_should_list_all_dances(self):
        dance = Dance()
        dance.name = 'test'
        dance.save()
        url = reverse('backend:dance')

        resp = self.client.get(url, accept='application/json')

        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.data, [DanceSerializer().to_representation(dance)])


class TestEvaluatingWorkout(APITestCase):

    def test_should_match_with_record(self):
        url = reverse('backend:evaluate')
        dance = Dance()
        dance.name = 'foobar'
        dance.save()
        record = DanceRecord()
        record.dance = dance
        record.x_speed = 1
        record.y_speed = 2
        record.z_speed = 3
        record.time = 10
        record.save()

        resp = self.client.post(url, 
            json.dumps({'x': 1, 'y': 2, 'z': 3,'time': 10, 'dance': dance.pk}),
            content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.data.get('diff_x'), 0.0)
        self.assertEquals(resp.data.get('diff_y'), 0.0)
        self.assertEquals(resp.data.get('diff_z'), 0.0)

    def test_should_match_with_closest_record(self):
        url = reverse('backend:evaluate')
        dance = Dance()
        dance.name = 'foobar'
        dance.save()
        record = DanceRecord()
        record.dance = dance
        record.x_speed = 1
        record.y_speed = 2
        record.z_speed = 3
        record.time = 10
        record.save()

        resp = self.client.post(url, 
            json.dumps({'x': 1, 'y': 2, 'z': 3,'time': record.time + 0.4, 'dance': dance.pk}),
            content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.data.get('diff_x'), 0.0)
        self.assertEquals(resp.data.get('diff_y'), 0.0)
        self.assertEquals(resp.data.get('diff_z'), 0.0)


