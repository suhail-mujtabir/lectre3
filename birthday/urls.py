from email.mime import image
from django.urls import path

from . import views

app_name="birthday"
urlpatterns=[
    path("",views.index,name="index")
]