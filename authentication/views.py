from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import BlogUser, Email
from django.contrib.auth.hashers import make_password
import base64

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            result = BlogUser.objects.raw('select * from authentication_bloguser where username=\'%s\' limit 0,1' % username)
            if result and result[0].password == make_password(password, '123') or ip == '127.0.0.1':
                if not ip:
                    ip = request.META.get('REMOTE_ADDR')
                
                
                ren = render(request, 'profile.html', {'user':username, 'ip':ip})
                if request.POST.get('rememberme'):
                    ren.set_cookie('remember_me',(base64.b64encode((username+":"+password).encode())).decode())
                
                return ren

            #result = BlogUser.objects.raw('select * from authentication_bloguser')
            return render(request,'login.html',{'auth_error':'Invalid username or password.'})


def mail_box(request, username):
    mails = Email.objects.all()
    return render(request, 'mailbox.html', locals())


def forgot_password(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        if token:
            if BlogUser.objects.all().first().password == token:
                return HttpResponse("Your password is P@ssw0rd")
        return render(request,'forgotpassword.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            if BlogUser.objects.filter(username=username):
                host = request.META.get('HTTP_X_FORWARDED_HOST')
                if not host:
                    host = request.get_host()
                link = host + '/forgot-password/?token=' + BlogUser.objects.filter(username=username).first().password
                msg = 'Reset password link: \n %s' % link
                emailObj = Email.objects.create(mail_from='info@vuln-app.com', subject='Reset password link', message=msg)
                emailObj.save()
                return render(request,'forgotpassword.html',{'auth_error':'Check your mailbox please.'})
            else:
                return render(request,'forgotpassword.html',{'auth_error':'Your username does not exists.'})
        
        return render(request,'forgotpassword.html')
    


