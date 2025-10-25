from django.db import models

# Create your models here.
class Invoice(models.Model):
    TRANSACTION_STATUS_CHOICES = (
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
        ('failed', 'Failed'),
    )
    invoice_id = models.CharField(max_length=100, unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=100, choices=TRANSACTION_STATUS_CHOICES, default='unpaid')
    created_at=models.DateTimeField(auto_now_add=True)

class Items(models.Model):
    invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    invoice_item=models.CharField(max_length=100)
    item_unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    def save(self, *args, **kwargs):
        self.total=self.item_unit_price*self.quantity
        super().save(*args, **kwargs)


class Transaction (models.Model):
    RECORD=(
        ('sold', 'Sold'),
        ('paid', 'Paid'),
    )
    invoice=models.ForeignKey(Invoice, on_delete=models.PROTECT)
    Transaction_status=models.CharField(max_length=100, choices=RECORD)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    Transaction_time=models.DateTimeField(auto_now_add=True)
