from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trademark_manager import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('Form3/', views.Form_3_APIViewList.as_view()),
    path('Form33/', views.Form_33_APIViewList.as_view()),
    path('Form2/', views.Form_2_APIViewList.as_view()),
    path('Form1/', views.Form_1_APIViewList.as_view()),
    path('Form22/', views.Form_22_APIViewList.as_view()),
    path('Form17/', views.Form_17_APIViewList.as_view()),
    path('Form12/', views.Form_12_APIViewList.as_view()),


    path('Form3/<int:pk>', views.Form_3_APIView.as_view()),
    path('Form33/<int:pk>', views.Form_33_APIView.as_view()),
    path('Form2/<int:pk>', views.Form_2_APIView.as_view()),
    path('Form1/<int:pk>', views.Form_1_APIView.as_view()),
    path('Form22/<int:pk>', views.Form_22_APIView.as_view()),
    path('Form17/<int:pk>', views.Form_17_APIView.as_view()),
    path('Form12/<int:pk>', views.Form_12_APIView.as_view()),
    path('File-Download/', views.FileDownload.as_view()),
    path('PDFGEN/<int:pk>', views.Form_1_PDFGEN.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
