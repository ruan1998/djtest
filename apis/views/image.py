import os
from django.views import View
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from workingflow_backend import settings
from utils.response import CommonResponse

class ImageView(View, CommonResponse):

    base_massage = ' method success'
    def get(self, request):
        image_name = request.GET.get('image_name')
        imgfile = os.path.join(settings.IMAGES_DIR, image_name + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            # data = open(imgfile,  'rb').read()
            return FileResponse(open(imgfile,  'rb'), content_type='image/jpg')

    def post(self, request):
        message = 'post' + self.base_massage
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = 'put' + self.base_massage
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        message = 'delete' + self.base_massage
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

def image(request):
    if request.method == 'GET':
        image_name = request.GET.get('image_name')
        imgfile = os.path.join(settings.IMAGES_DIR, image_name + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            # data = open(imgfile,  'rb').read()
            return FileResponse(open(imgfile,  'rb'), content_type='image/jpg')

def image_text(request):
    if request.method == 'GET':
        image_name = request.GET.get('image_name')
        imgfile = os.path.join(settings.IMAGES_DIR, image_name + '.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(
                    code=utils.result.ReturnCode.RESOURCE_NOT_EXISTS)
        else:
            response_data = {}
            response_data['name'] = image_name + '.jpg'
            response_data['url'] = '/service/image?md5=%s' % image_name
            response = utils.response.wrap_json_response(data = response_data)
            return JsonResponse(data=response, safe=False)
