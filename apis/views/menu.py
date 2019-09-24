import os
import yaml
from django.http import JsonResponse
from workingflow_backend import settings
from utils.response import CommonResponse, ReturnCode
from django.shortcuts import render

def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps

def get_menu(request):
    global_app_data = init_app_data()
    published_app_date = global_app_data.get('published')
    response = CommonResponse.wrap_json_response(data=published_app_date,
                                                 code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)
