from django.urls import path
from Patent_manager import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('ammendement-action/', views.AmendementAction_view.as_view()),
    path('ammendement-action/<int:pk>', views.AmendementAction_view.as_view()),
    
    path('assignment-merger-action/', views.AssignmentMergerAction_view.as_view()),
    path('assignment-merger-action/<int:pk>', views.AssignmentMergerAction_view.as_view()),


    path('change-address/', views.ChangeOfAddress_view.as_view()),
    path('change-address/<int:pk>', views.ChangeOfAddress_view.as_view()),

    path('change-name/', views.ChangeOfName_view.as_view()),
    path('change-name/<int:pk>', views.ChangeOfName_view.as_view()),

    path('ctc/', views.CTC_view.as_view()),
    path('ctc/<int:pk>', views.CTC_view.as_view()),

    path('patent-particulars/', views.PatentParticulars_view.as_view()),
    path('patent-particulars/<int:pk>', views.PatentParticulars_view.as_view()),

    path('procurement/', views.ProcurementOfCertification_view.as_view()),
    path('procurement/<int:pk>', views.ProcurementOfCertification_view.as_view()),

    path('registration/', views.Registration_view.as_view()),
    path('registration/<int:pk>', views.Registration_view.as_view()),

    path('renewal-action/', views.Renewals_view.as_view()),
    path('renewal-action/<int:pk>', views.Renewals_view.as_view()),

    path('search-action/', views.Search_view.as_view()),
    path('search-action/<int:pk>', views.Search_view.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
