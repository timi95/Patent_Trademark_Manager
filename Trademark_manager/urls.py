from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('amendement-action/', views.AmendementActionViewLC.as_view()),
    path('amendement-action/', views.AmendementActionViewRUD.as_view()),

    path('assignment-merger-action/', views.AssignmentMergerActionViewLC.as_view()),
    path('assignment-merger-action/', views.AssignmentMergerActionViewRUD.as_view()),

    path('certificate-procurement-action/', views.CertificateProcurementActionViewLC.as_view()),
    path('certificate-procurement-action/', views.CertificateProcurementActionViewRUD.as_view()),

    path('change-name-address-action/', views.ChangeName_AddressActionViewLC.as_view()),
    path('change-name-address-action/', views.ChangeName_AddressActionViewRUD.as_view()),

    path('profile/', views.TrademarkProfileViewLC.as_view()),
    path('profile/', views.TrademarkProfileViewRUD.as_view()),

    path('registration-action/', views.RegistrationActionViewLC.as_view()),
    path('registration-action/', views.RegistrationActionViewRUD.as_view()),

    path('renewal-action/', views.RenewalActionViewLC.as_view()),
    path('renewal-action/', views.RenewalActionViewRUD.as_view()),

    path('search-action/', views.SearchActionViewLC.as_view()),
    path('search-action/', views.SearchActionViewRUD.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
