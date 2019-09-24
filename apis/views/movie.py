from django.http import HttpResponse, JsonResponse
from django.views import View
from thirdparty import juhe
import json
from utils.response import CommonResponse

# def helloworld(request):
#     print('request method: ', request.method)
#     print('request META: ', request.META)
#     print('request cookies: ', request.COOKIES)
#     m = [1,2,3]
#     return JsonResponse(data=m, safe=False, status=200)
#     pass

# def movie(request):
#     if request.method == 'GET':
#         moviename =request.GET.get('title')
#         if moviename:
#             data = juhe.movie(moviename)
#             return JsonResponse(data=dict(data), safe=False, status=200)
#     elif request.method == 'POST':
#         received_body = request.body()
#         received_body = json.load(received_body)
#         movies = received_body.get('title')
#         for mov in movies:
#             result = juhe.weather(mov)
#             response_data.append(result)
#         return JsonResponse(data =response_data, safe=False, status=200)

class MovieView(View, CommonResponse):

    def get(self, request):
        pass

    def post(self, request):
        received_body = request.body()
        received_body = json.load(received_body)
        movies = received_body.get('title')
        for mov in movies:
            result = juhe.weather(mov)
            response_data.append(result)
        response_data = self.wrap_json_response(data=response_data)
        return JsonResponse(data=response_data, safe=False, status=200)
