"""Bike_CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pages.views import home_view,contact_view,about_view,booking_view ##use this format to import in case have multiple apps to import from it will be confustin


urlpatterns = [
	path('', home_view),
	path('home/', home_view), 
	path('contacts/', contact_view),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    path('booking/', booking_view),

]
##this is a test for git
