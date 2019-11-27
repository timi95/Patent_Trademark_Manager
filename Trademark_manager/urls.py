from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('profile/', views.TrademarkProfile_view.as_view()),
    path('particulars/', views.TrademarkParticulars_view.as_view()),
    path('action1/', views.TrademarkAction2_view.as_view()),
    path('action2/', views.TrademarkAction1_view.as_view()),
    path('full_profile/', views.Profile_Actions_Relative_view.as_view()),
    path('full_profile_RUD/<int:pk>', views.Profile_Actions_Relative_RUD_view.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)
