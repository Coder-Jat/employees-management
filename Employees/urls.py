"""
URL configuration for Employees project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views
from Employees_detail.views import get_details

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('employees/', include('Employees_detail.urls')),
    
    path('', views.employee_list, name='employee_list'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path("__reload__", include("django_browser_reload.urls")),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
