"""communify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from communify import views
from django.conf import settings
from django.conf.urls.static import static
from login import urls 
from .views import feed_redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name="index"),
    #path('login/', views.Login, name="login"),
    #path('create/', views.Create, name="create"),
    #path('post/', views.Post, name="post"),
    path('message/', views.Message, name="message"),
    path('login/forgot/', views.Forgotpass, name="forgotpass"),
    path('about/', views.About, name="about"),
    path('contact/', views.Contact, name="contact"),
    path('feed/', include('posts.urls', namespace='posts')),
    path('account/', include('login.urls')),
    path('login/', include('login.urls', namespace='signIn')),
    #path('account/', include('django.contrib.auth.urls')),
    path("", include("allauth.urls")),
    path('social/feed/',feed_redirect, name= 'feed_redirect'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)