from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import json

from .models import Record

class SaveDataAPI(APIView):

    def post(self, request, *args, **kwargs):
        record = Record(json_data=json.dumps(request.data))
        record.save()
        return Response({'message': 'ok'})
