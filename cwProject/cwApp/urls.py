from django.urls import path
from . import views

urlpatterns = [
    # welcome page
    path('', views.index, name='index'),
    # add to model
    path('application', views.application, name='application'),
    # confirmation
    path('confirmation', views.confirmation, name='confirmation'),
]
