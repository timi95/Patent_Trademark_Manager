from rest_framework import generics, filters
# from django_filters.rest_framework import DjangoFilterBackend,DateTimeFromToRangeFilter
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.response import Response
import asyncio

# Create your views here.

# Patent Particulars 
class ReminderViewLC(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = Reminder_serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get(self, request, *args, **kwargs):
        if request.query_params and list(iter(request.query_params))[0] == 'date_from':
            self.queryset = Reminder.objects.filter(
            reminder_date__range=[
            self.request.query_params['date_from'],
            self.request.query_params['date_to'] ])              
        return super().get(request, *args, **kwargs)    
    

class ReminderViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = Reminder_serializer
    

async def reminder_monitoring():
    for reminder in Reminder.objects.all():
        print('async function called, reminder here',reminder)
    
    # wait for a while then call the function again
    # await asyncio.sleep(5)
    # await reminder_monitoring()


# asyncio.run(reminder_monitoring())