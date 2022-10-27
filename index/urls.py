from django.urls import path
from . import views
app_name="index"
urlpatterns=[
    path("",views.index,name="index")
]
handler404 = "index.views.page_not_found_view"