from django import forms
from schedule.models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields='__all__'
        widgets ={
            "start_time": forms.TextInput(attrs={"type":"time"}),
            "end_time": forms.TextInput(attrs={"type":"time"})
        }