"""Patent_Trademark_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

project_name = "Allan & Ogunkeye's Patent and Trademark manager"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_swagger_view(title=project_name)),
    path('documents/', include_docs_urls(title=project_name)),

    path('ApplicationForm_manager/', include('ApplicationForm_manager.urls')),
    path('Patent_manager/', include('Patent_manager.urls')),
    path('Trademark_manager/', include('Trademark_manager.urls'))
]
