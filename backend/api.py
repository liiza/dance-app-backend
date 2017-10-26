from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import logging
import json

from .models import Record, Dance, DanceRecord
from .serializers import DanceSerializer

logger = logging.getLogger(__name__)

class SaveDataAPI(APIView):

    def post(self, request, *args, **kwargs):
        record = Record(json_data=request.data)
        record.save()
        return Response({'message': 'ok'})

class DanceAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):
        dances = Dance.objects.all()
        serializer = DanceSerializer()
        return Response([serializer.to_representation(dance) for dance in dances])

    def post(self, request, *args, **kwargs):
        logger.warn(request.data) 
        dance = Dance(name=request.data.get('name'))
        dance.save()
        return Response({'pk': dance.pk})

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


