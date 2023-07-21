from django.urls import path
from . import views

urlpatterns = [
    path('all-participants/', views.all_participants_views),
    path('<int:id>/payments/', views.participatns_payments),
    path('<str:email>/', views.participant_detail)
]
