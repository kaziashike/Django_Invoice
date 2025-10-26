from rest_framework import serializers
from .models import Invoice, Items, Transaction

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        read_only_fields = ['invoice', 'total']


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['amount']

    def save(self, **kwargs):
        total_amount=0
        invoice=super().save(**kwargs)
        item_data=self.validated_data.get('items')
        if not item_data:
            raise serializers.ValidationError({"items": "Invoice must have at least one item."})
        
        for item in item_data:
            total_price=item['item_unit_price']*item['quantity']
            total_amount+=total_price

            Items.objects.create(invoice= invoice, invoice_item=item.get('invoice_item'), item_unit_price=item.get('item_unit_price'), quantity=item.get('quantity'), total=total_price)

        invoice.amount=total_amount
        invoice.save()
        return invoice


class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'