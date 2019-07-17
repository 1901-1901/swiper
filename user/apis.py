from django.http import JsonResponse
from common import errors
from common.utils import is_phone_num
from libs.http import render_json
from user import logics


def verify_phone(request):

    phone_num = request.POST.get('phone_num')

    if is_phone_num(phone_num):
        # 生成验证码
        # 发送验证码
        if logics.send_verify_code(phone_num):
            return render_json()
        else:
            return render_json(code=errors.SMS_SEND_ERR)
    else:
        return render_json(code=errors.PHONE_NUM_ERR)


def login(request):
    '''
    通过验证码登录或注册接口
    如果手机存在，则登录，否则，注册
    # 1.检测验证码是否正确
    # 2.注册或登录
    :param request:
    :return:
    '''
    