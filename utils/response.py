
class ReturnCode:
    SUCCESS = 0
    FAILED = -100
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARMAS = -101

    @classmethod
    def message(self, code):
        if code == self.SUCCESS:
            return 'success'
        elif code == self.FAILED:
            return 'failed'
        elif code == self.UNAUTHORIZED:
            return 'unauthorized'
        elif code == self.WRONG_PARMAS:
            return 'wrong params'
        else:
            return ''

class CommonResponse(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.message(code)
        if data:
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response
