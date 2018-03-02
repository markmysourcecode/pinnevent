from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('login/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
]