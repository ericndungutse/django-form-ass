from django.urls import path
from payment import views

urlpatterns = [
    path('all-payment/', views.payment_list),
    path('average-payments/', views.average_price_of_paid_events)
]
