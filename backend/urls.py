from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^dance$', api.DanceAPI.as_view(), name='dance'),
    url(r'^record$', api.AddRecordToDance.as_view(), name='record'),
    url(r'^evaluate$', api.EvaluateExercise.as_view(), name='evaluate'),
]
