from rest_framework import serializers
from .models import Invoice, Items, Transaction

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        read_only_fields = ['invoice', 'total']


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        if not items_data:
            raise serializers.ValidationError({"items": "Invoice must have at least one item."})

        invoice = Invoice.objects.create(**validated_data)

        total_amount = 0
        for item in items_data:
            total_price = item['item_unit_price'] * item['quantity']
            total_amount += total_price

            Items.objects.create(
                invoice=invoice,
                invoice_item=item['invoice_item'],
                item_unit_price=item['item_unit_price'],
                quantity=item['quantity'],
                total=total_price
            )

        invoice.amount = total_amount
        invoice.save()
        return invoice


class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'