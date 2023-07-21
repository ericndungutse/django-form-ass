from django.shortcuts import render
from participant.models import Participant
from django.http import HttpResponse
from payment.models import Payment

def all_participants_views(request):
    participants = Participant.objects.all()
    return render(request, 'participant/participants.html', {'participants': participants})


def participant_detail(request, email):
    participant = Participant.objects.get(email=email)
    return render(request, 'participant/participant.html', {"participant":participant})

def participatns_payments(request,id):
    participantId = str(id)
    payments = Payment.objects.filter(participant_id=participantId)
    pay_response = ' '

    for payment in payments:
        pay_response = pay_response + str(payment.amount_paid) + ', '

    return HttpResponse(pay_response)

