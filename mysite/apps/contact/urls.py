from django.conf.urls import url
from django.http import JsonResponse
import json

def test(req):
    return JsonResponse({'status': 201, 'message': 'success'})

urlpatterns = [
    url(r'^test', test, name="submit"),
]
