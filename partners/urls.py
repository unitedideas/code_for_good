from django.urls import path, include

from . import views

app_name = 'lobosevents'

urlpatterns = [

    path('partner_form', views.partner_form, name='partner_form'),
    path('diaper_request', views.diaper_request, name='diaper_request'),

]
