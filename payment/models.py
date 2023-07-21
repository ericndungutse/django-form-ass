from django.db import models
from participant.models import Participant
from event.models import Event


# Create your models here.
class Payment(models.Model):
    payment_status_choices = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed','Failed')
    )

    payment_methods_choices = (
        ('visa', 'Visa'),
        ('momo', 'MoMo')
    )


    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=payment_methods_choices)
    payment_date = models.DateTimeField()
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=payment_status_choices)

    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
