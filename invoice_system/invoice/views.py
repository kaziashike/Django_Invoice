from django.shortcuts import render
from .models import Invoice, Items, Transaction
from .serializer import InvoiceSerializer, ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create invoice (Post)
@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        invoice = serializer.save()
        return Response(InvoiceSerializer(invoice).data, status=201)
    return Response(serializer.errors, status=400)

# Pay Invoice (Post)
@api_view(['POST'])
def pay_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    if invoice.status == 'unpaid':
        invoice.status = 'paid'
        invoice.save()
        # Create transaction record
        transaction = Transaction.objects.create(
            Transaction_status='paid',
            amount=invoice.amount,
            invoice=invoice
        )
        return Response({'message': 'Invoice paid successfully'})
    else:
        return Response({'error': 'Invoice is already paid'}, status=400)

# Get single invoice (Get)
@api_view(['GET'])
def get_single_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    serializer = InvoiceSerializer(invoice)
    return Response(serializer.data)

# List all invoices (Get)
@api_view(['GET'])
def get_invoices(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

# Delete invoice
@api_view(['DELETE'])
def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    invoice.delete()
    return Response({'message': 'Invoice deleted successfully'}, status=204)