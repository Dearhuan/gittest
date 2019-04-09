from django.shortcuts import render
from django.http import HttpResponse
from lib.sms import send_sms

# Create your views here.
def submit(request):
    '''获取短信验证码'''
    if not request.method == 'POST':
        return HttpResponse('request method error')
    phone = request.POST.get('phone')
    result,msg = send_sms(phone)
    print(msg)
    return HttpResponse('send success')

def submit(request):
    '''通过验证码登录注册'''
    pass
def submit(request):
    '''获取个人资料'''
    pass
def submit(request):
    '''修改个人资料'''
    pass
def submit(request):
    '''头像上传'''
    pass
