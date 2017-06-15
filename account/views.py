# coding=utf-8

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from account.models import  User
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

@csrf_exempt
def register(request):
    if request.method == 'POST':
        if 'username' in request.POST :
            username= request.POST['username']
            Password= request.POST['password']
            User.objects.create(username= username,password=Password)
            #注册成功发送邮件
            # subject="祝贺你成功注册"
            # message="congratulations!"
            # send_mail(subject,message,'917829801@qq.com',['397697774@qq.com'])
            #注册成功返回页面
            return HttpResponse('regist success!!'+username)
    else:
        pass
    return render_to_response('register.html' )

def login(req):
    if req.method == 'POST':
       if req.POST :
           username =req.POST['Username']
           password =req.POST['Password']
           user = User.objects.filter(username__exact = username,password__exact = password)
           if user:
               response = HttpResponseRedirect('index/')
               response.set_cookie('username',username,3600)
               return response
           else:
               return HttpResponseRedirect('/account/login/')
    else:
        return render_to_response('login.html')

def index(req):
     username = req.COOKIES.get('username','')
     return render_to_response('index.html' ,{'username':username})

def logout(req):
    response = HttpResponse('logout!!')
    response.delete_cookie('username')
    return response



