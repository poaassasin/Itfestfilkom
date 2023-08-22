"""itfest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('viewer', TemplateView.as_view(template_name='viewer.html'), name='index'),
    path('user/', include('home.urls')),
    path("more_bisnis/", TemplateView.as_view(template_name="more_bisnis.html"), name='more_bisnis'),
    path("more_uiux/", TemplateView.as_view(template_name="more_uiux.html"), name='more_uiux'),
    path('admin/', admin.site.urls),
]
