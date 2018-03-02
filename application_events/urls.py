from django.urls import path
from application_events import views

app_name = 'application_events'

urlpatterns = [
    path('', views.ThankYouView, name='thanksfor'),
    path('<thanks_for>/', views.ThankYouView, name='thanksfor'),
]