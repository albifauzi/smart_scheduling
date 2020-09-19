from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('schedule', views.schedule, name='schedule'),
    path('thanks', views.thanks, name='thanks'),
]