from django.shortcuts import render
from speaker.models import Speaker
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
        pass
    else:
        form = SpeakerForm()
        context={"form": form }
    return render(request, 'speaker/addSpeakerForm.html', context)
