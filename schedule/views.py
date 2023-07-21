from django.shortcuts import render
from schedule.models import Schedule
# Create your views here.
def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule.html', {'schedules': schedules})


