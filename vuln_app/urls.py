"""vuln_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from blog import views as blogViews
from authentication import views as authenticationViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blogViews.blog, name='blog'),
    path('blog/<int:id>/', blogViews.post, name='post'),
    path('login/', authenticationViews.login, name='login'),
    path('mailbox/<str:username>/', authenticationViews.mail_box, name='mailbox'),
    path('forgot-password/', authenticationViews.forgot_password, name='forgotpassword'),
    path('',blogViews.blog, name='home')
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
