from django.shortcuts import render
from payment.models import Payment
from payment.form import PaymentForm
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

def Payment_Form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        form.save()
        if form.is_valid:
            return HttpResponse('payment added')
        else:
            return HttpResponse('not valid')
    else:
    
        form = PaymentForm()
        context={"form": form }
    return render(request, 'payment/paymentform.html', context)
