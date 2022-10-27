from django.shortcuts import render



app_name="index"
def index(request):
    return render(request,"index/index.html",{
        "home":True,
    })
def page_not_found_view(request, exception):
    return render(request, "index/404.html", status=404)

