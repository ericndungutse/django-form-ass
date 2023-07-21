from django.shortcuts import render
from schedule.models import Schedule
from schedule.forms import ScheduleForm
# Create your views here.
def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule.html', {'schedules': schedules})

def schedule_form(request):
    if request.method == 'POST':
        pass
    else:
        form = ScheduleForm()
        context={"form": form }
    return render(request, 'schedule/addscheduleform.html', context)


