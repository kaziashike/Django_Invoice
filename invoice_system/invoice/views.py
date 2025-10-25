from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create invoice (Post)
@api_view(['POST'])
def create_invoice(request):
    serializer=InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        Invoice= serializer.save()
        return Response(InvoiceSerializer(Invoice).data)
    return Response(serializer.errors, status= 400)
# pay Invoice (Post)
@api_view(['POST'])
def  pay_invoice(request, invoice_id):
    serializers=InvoiceSerializer(request.data)
    Invoice=get_object_or_404(Invoice,invoice_id=invoice_id)
    if  serializers.is_valid():
        if (Invoice.status == 'unpaid'):
            Invoice.status = 'paid'
            Invoice.save()
            transaction=Transaction.objects.create(Transaction_status='paid', amount=Invoice.amount, invoice=Invoice)
        else:
            return Response({'error': 'Invoice is already paid'})
    else:
        return Response(serializers.errors)
# single list invoice (Get)
@api_view(['GET'])
def get_single_invoice(request,invoice_id):
    invoice=get_object_or_404(Invoice, invoice_id=invoice_id)
    serializers=InvoiceSerializer(invoice)
    return Response(serializers.data)
# list all invoice (Get)
@api_view(['GET'])
def get_invoices(request):
    invoice=Invoice.objects.all()
    serrializer=InvoiceSerializer(invoice, many=True)
    return Response(serrializer.data)