from django.urls import path
from Patent_manager import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('patent', views.PatentParticulars_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
