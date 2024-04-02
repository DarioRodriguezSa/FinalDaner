from django.urls import path

from . import views

app_name = "Apps.reportes_generales"
urlpatterns = [
  
    path('', views.general, name='index'),
]