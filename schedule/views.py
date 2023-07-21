from django.shortcuts import render
from schedule.models import Schedule
from schedule.forms import ScheduleForm
from django.http import HttpResponse
# Create your views here.
def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule.html', {'schedules': schedules})

def schedule_form(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        form.save()
        if form.is_valid:
            return HttpResponse('schedule added')
        else:
            return HttpResponse('not valid')
    else:
    
        form = ScheduleForm()
        context={"form": form }
    return render(request, 'schedule/addscheduleform.html', context)



