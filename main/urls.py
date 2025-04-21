from django.urls import path
from .views import home_view, about, echo

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about, name='about'),
    path('echo/', echo, name='echo'),
]