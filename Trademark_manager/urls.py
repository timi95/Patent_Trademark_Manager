from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('profile/', views.TrademarkProfile_view.as_view()),
    path('ammendement/', views.AmendementAction_view.as_view()),
    path('assignment-merger/', views.AssignmentMergerAction_view.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
