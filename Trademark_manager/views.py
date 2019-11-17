from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from Patent_Trademark_Strings.Trademarks_Act_Form_33_String import Form33StringClass
import pdfkit


# Create your views here.
class Form_3_APIViewList(generics.ListAPIView):
    queryset = Form_3_Model.objects.all()
    serializer_class = Form_3_serializer


class Form_33_APIViewList(generics.ListAPIView):
    queryset = Form_33_Model.objects.all()
    serializer_class = Form_33_serializer


class Form_2_APIViewList(generics.ListAPIView):
    queryset = Form_2_Model.objects.all()
    serializer_class = Form_2_serializer

class Form_22_APIViewList(generics.ListAPIView):
    queryset = Form_22_Model.objects.all()
    serializer_class = Form_22_serializer


class Form_17_APIViewList(generics.ListAPIView):
    queryset = Form_17_Model.objects.all()
    serializer_class = Form_17_serializer


class Form_12_APIViewList(generics.ListAPIView):
    queryset = Form_12_Model.objects.all()
    serializer_class = Form_12_serializer

class Form_1_APIViewList(generics.ListAPIView):
    queryset = Form_1_Model.objects.all()
    serializer_class = Form_1_serializer






class Form_3_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_3_Model.objects.all()
    serializer_class = Form_3_serializer


class Form_33_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_33_Model.objects.all()
    serializer_class = Form_33_serializer


class Form_2_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_2_Model.objects.all()
    serializer_class = Form_2_serializer

class Form_22_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_22_Model.objects.all()
    serializer_class = Form_22_serializer


class Form_17_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_17_Model.objects.all()
    serializer_class = Form_17_serializer


class Form_12_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_12_Model.objects.all()
    serializer_class = Form_12_serializer

class Form_1_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form_1_Model.objects.all()
    serializer_class = Form_1_serializer



class FileDownload(APIView):
    def get(self, request, format=None):
        print("this is to test that this function ran on this API call")
        # generate the file
        try:
            return FileResponse(
            open('/home/psykinetic/workspace/Python_and_Django/sample.pdf', 'rb'),
            content_type='application/pdf'
            )
        except FileNotFoundError:
            raise Http404()


def FileFactory(APIView):
    print("FileFactory activating")
    filename = "example.pdf"
    input = Form_33_Model.objects.create().html.replace("\n", "")
    return pdfkit.from_string(input, f"{filename}")
