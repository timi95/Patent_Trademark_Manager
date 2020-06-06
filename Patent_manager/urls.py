from django.urls import path
from Patent_manager import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('ammendement-action/', views.AmendementActionViewLC.as_view()),
    path('ammendement-action/<int:pk>', views.AmendementActionViewRUD.as_view()),
    
    path('assignment-merger-action/', views.AssignmentMergerActionViewLC.as_view()),
    path('assignment-merger-action/<int:pk>', views.AssignmentMergerActionViewRUD.as_view()),


    path('change-address/', views.ChangeOfAddressViewLC.as_view()),
    path('change-address/<int:pk>', views.ChangeOfAddressViewRUD.as_view()),

    path('change-name/', views.ChangeOfNameViewLC.as_view()),
    path('change-name/<int:pk>', views.ChangeOfNameViewRUD.as_view()),

    path('ctc/', views.CTCViewLC.as_view()),
    path('ctc/<int:pk>', views.CTCViewRUD.as_view()),

    path('patent-particulars/', views.PatentParticularsViewLC.as_view()),
    path('patent-particulars/<int:pk>', views.PatentParticularsViewRUD.as_view()),

    path('procurement/', views.ProcurementOfCertificationViewLC.as_view()),
    path('procurement/<int:pk>', views.ProcurementOfCertificationViewRUD.as_view()),

    path('registration/', views.RegistrationViewLC.as_view()),
    path('registration/<int:pk>', views.RegistrationViewRUD.as_view()),

    path('renewal-action/', views.RenewalsViewLC.as_view()),
    path('renewal-action/<int:pk>', views.RenewalsViewRUD.as_view()),

    path('search-action/', views.SearchViewLC.as_view()),
    path('search-action/<int:pk>', views.SearchViewRUD.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
