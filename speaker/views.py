from django.shortcuts import render
from speaker.models import Speaker
# Create your views here.
def all_speakers(request):
    speaker = Speaker.objects.all()
    return render(request, 'speaker/all_speakers.html', {'speaker': speaker})

def speaker_detail( request, name):
        speaker = Speaker.objects.get(name=name)
        return render(request, 'speaker/speakerdetail.html', {'speaker': speaker})
