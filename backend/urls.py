from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^momentary-speed$', api.SaveDataAPI.as_view(), name='momentary_speed'),
    url(r'^dance$', api.CreateDanceAPI.as_view(), name='dance'),
    url(r'^record$', api.AddRecordToDance.as_view(), name='record'),
]
