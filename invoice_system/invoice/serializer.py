from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'


class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'