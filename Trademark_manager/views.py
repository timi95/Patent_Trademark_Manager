from django.shortcuts import render
from django.http import FileResponse, HttpResponse, Http404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from Patent_Trademark_Strings.Trademarks_Act_Form_33_String import Form33StringClass
import pdfkit
import os

# Create your views here.
# GET
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




# GET<Id>, POST, DELETE

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


# PDF GENERATORS

class Form_1_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_1_Model.objects.all()
    serializer_class = Form_1_serializer

    def get(self, request, pk):
        filename = f'Form_1_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_2_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_2_Model.objects.all()
    serializer_class = Form_2_serializer

    def get(self, request, pk):
        filename = f'Form_2_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_3_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_3_Model.objects.all()
    serializer_class = Form_3_serializer

    def get(self, request, pk):
        filename = f'Form_3_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_12_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_12_Model.objects.all()
    serializer_class = Form_12_serializer

    def get(self, request, pk):
        filename = f'Form_12_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_17_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_17_Model.objects.all()
    serializer_class = Form_17_serializer

    def get(self, request, pk):
        filename = f'Form_17_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_22_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_22_Model.objects.all()
    serializer_class = Form_22_serializer

    def get(self, request, pk):
        filename = f'Form_22_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


class Form_33_PDFGEN(generics.RetrieveAPIView):
    queryset = Form_33_Model.objects.all()
    serializer_class = Form_33_serializer

    def get(self, request, pk):
        filename = f'Form_33_PDF_ID_{pk}.pdf'
        input = self.get_object().html

        try:
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            pdfkit.from_string(input, f"Trademark_manager/GeneratedForms/{filename}", configuration=config)
            pdf = open(f"Trademark_manager/GeneratedForms/{filename}", "rb")
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            pdf.close()
            os.remove(f"Trademark_manager/GeneratedForms/{filename}")
            return response
        except FileNotFoundError:
            raise Http404()


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
