from django.shortcuts import render
from payment.models import Payment
from payment.models import Payment
from django.http import HttpResponse
from django.db.models import Avg

# Create your views here.
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/all_payments_list.html', {'payments': payments})

# Create your views here.
def average_price_of_paid_events(request):
    averageAmountPaid = Payment.objects.aggregate(Avg('amount_paid'))
    responseTxt = 'Average amount paid is ' + str(averageAmountPaid['amount_paid__avg'])
    return HttpResponse(responseTxt)
