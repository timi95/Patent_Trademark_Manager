from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('profile/', views.TrademarkProfile_view.as_view()),
    path('ammendement-action/', views.AmendementAction_view.as_view()),
    path('assignment-merger-action/', views.AssignmentMergerAction_view.as_view()),
    path('certificate-procurement-action/', views.CertificateProcurementAction_view.as_view()),
    path('change-name-address-action/', views.ChangeName_AddressAction_view.as_view()),
    path('registration-action/', views.RegistrationAction_view.as_view()),
    path('renewal-action/', views.RenewalAction_view.as_view()),
    path('search-action/', views.SearchAction_view.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
