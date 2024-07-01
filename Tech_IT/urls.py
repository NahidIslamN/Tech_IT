"""
URL configuration for Tech_IT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Functions.views import *
from Authentications.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about_us/', AboutPage.as_view(), name='about_page'),
    path('admin/', admin.site.urls),
    path('learnmoreaboutus/',LearnmoreAboutpage.as_view(), name='learnmoreaboutus'),
    path('services/', ServicePage.as_view(), name ='services' ),
    path('teams/', TeamPage.as_view(), name='teams'),
    path('portfolio/', OurPortfolio.as_view(), name='portfolio'),
    path('pricing/', Pricings.as_view(), name = 'pricing'),
    path('contuct_us/', ContactUs.as_view(), name = 'contuct_us'),


    path('learmore_services/', learnMore.as_view(), name = 'learmore_services'),
    path('inbox/', PublicMessages.as_view(), name = "inbox"),

    path("subscribe/", Subscirber.as_view(), name = 'subscribe'),
    
    

    #Authentication
    path('login/', Loging_Page.as_view(), name="login_user_deshboard"),
    path('logout/', LogoutRout.as_view(), name='logout'),
   
]

if settings.DEBUG:
       
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
