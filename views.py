from django.shortcuts import render
from rest_framework.views import APIView
from rtv_module.models import PayoutCountModel
from rtv_module.serializers import PayoutCountSerializer
from rest_framework.response import Response
from csv2pdf import convert
import pypandoc
import pdfkit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
# Create your views here.

class PayoutWiseCountView(APIView):
    def post(self, request):
        payoutquery = PayoutCountModel.objects.all()
        print(payoutquery)
        payoutserializer = PayoutCountSerializer(payoutquery, many = True)
        print(payoutserializer.data)
        return Response(data = {'message':'Successfully fetch ! ', 'formdata':payoutserializer.data})
    
class Csv2PDF(APIView):
    def post(self, request):
        print('request : ', request.data)
        # convert("E:\prodigi_sub_scenario_master.csv", "E:\destination.pdf", orientation="L", align="C", size=8, headersize=10)
        pdf = SimpleDocTemplate("E:\dataframe.pdf", pagesize=letter)
        data = pd.read_csv("E:\prodigi_sub_scenario_master.csv")
        table_data = []
        for i, row in data.iterrows():
            table_data.append(list(row))

        table = Table(table_data)
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ])

        table.setStyle(table_style)
        pdf_table = []
        pdf_table.append(table)
        print('pdf_table : ', pdf_table)
        pdf.build(pdf_table)
        return Response({'message': 'Converted'})

# this is my feature-2-brance code.

        
