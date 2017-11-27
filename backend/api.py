from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import logging
import json

from .models import Dance, DanceRecord
from .serializers import DanceSerializer

logger = logging.getLogger(__name__)


class DanceAPI(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):
        dances = Dance.objects.all()
        serializer = DanceSerializer()
        return Response([serializer.to_representation(dance) for dance in dances])

    def post(self, request, *args, **kwargs):
        dance = Dance(name=request.data.get('name'))
        dance.save()
        return Response({'pk': dance.pk})

class EvaluateExercise(APIView):

    def post(self, request, *args, **kwargs):
        json = request.data
        dance = Dance.objects.get(pk=json.get('dance'))
        if not dance:
            raise Exception("No dance found")

        time = json.get('time')
        lower_limit = time - 100
        upper_limit = time + 500
        record = DanceRecord.objects.filter(dance=dance.pk, time__gt=lower_limit, time__lt=upper_limit).first()
        if not record:
            return Response({'ended': True})

        diff_x = record.x_speed - json.get('x')
        diff_y = record.y_speed - json.get('y')
        diff_z = record.z_speed - json.get('z')

        return Response({'ended': False, 'diff_x': diff_x, 'diff_y': diff_y, 'diff_z': diff_z})

class AddRecordToDance(APIView):

    def post(self, request, *args, **kwargs):
        json = request.data
        dance = Dance.objects.get(pk=json.get('dance'))
        if not dance:
            return Response(status=400)

        record = DanceRecord()
        record.dance = dance
        record.x_speed=json.get('x')
        record.y_speed=json.get('y')
        record.z_speed=json.get('z')
        record.time = json.get('time')
        record.save()
        return Response({'pk': record.pk})


