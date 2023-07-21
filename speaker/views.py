from django.shortcuts import render
from speaker.models import Speaker
from django.http import HttpResponse
from .forms import SpeakerForm

# Create your views here.
def all_speakers(request):
    speaker = Speaker.objects.all()
    return render(request, 'speaker/all_speakers.html', {'speaker': speaker})

def speaker_detail( request, name):
        speaker = Speaker.objects.get(name=name)
        return render(request, 'speaker/speakerdetail.html', {'speaker': speaker})

def add_speaker_form_view(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        form.save()
        if form.is_valid:
            return HttpResponse('Speaker added')
        else:
            return HttpResponse('not valid')
    else:
        form = SpeakerForm()
        context={"form": form }
    return render(request, 'speaker/addSpeakerForm.html', context)