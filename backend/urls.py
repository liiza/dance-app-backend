from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^momentary-speed$', views.SaveDataAPI.as_view(), name='momentary_speed'),
]
