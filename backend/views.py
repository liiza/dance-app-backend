from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import logging
import json

from .models import Record

logger = logging.getLogger(__name__)

class SaveDataAPI(APIView):

    def post(self, request, *args, **kwargs):
        logger.warn(request.body)       
        record = Record(json_data=json.dumps(request.body))
        record.save()
        return Response({'message': 'ok'})
