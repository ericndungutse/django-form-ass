from django.urls import path
from event import views

urlpatterns = [
    path('all-events/', views.all_events_view),
    path('free-events/', views.list_of_free_events),
    path('paid-events/', views.list_of_paid_events),
    path('add-event/', views.add_event_view),
    path('<str:title>/', views.one_event_view),
    path('<int:id>/speakers/', views.speaker_of_specific_event),
    path('<int:id>/total-amout-paid', views.total_amount_paid_for_specific_event),
    path('schedules/<int:id>', views.schedules_of_specific_event),
]
