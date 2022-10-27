from django.urls import path
from . import views
app_name="user"
urlpatterns=[
    path("",views.login,name="login"),
    path("new login/",views.newlogin,name="newlogin")
]