from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [

]

urlpatterns = format_suffix_patterns(urlpatterns)
