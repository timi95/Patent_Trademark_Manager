from django.urls import path
from Reminders import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('reminder/', views.ReminderViewLC.as_view()),
    path('reminder/<int:pk>', views.ReminderViewRUD.as_view())
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
