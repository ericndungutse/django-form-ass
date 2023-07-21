from django.urls import path
from speaker import views

urlpatterns = [
    path('all-speakers/', views.all_speakers, name=''),
    path('<str:name>/', views.speaker_detail, name='')
]