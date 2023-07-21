from django.urls import path
from schedule import views

urlpatterns = [
    path('all-schedules/', views.schedule,name=''),
    path('add-schedule/', views.schedule_form),
]