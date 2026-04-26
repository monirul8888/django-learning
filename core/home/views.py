from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    peoples = [
        {"name" : "Monirul", "dept": "CSE"},
        {"name" : "Akib", "dept": "CSE"},
        {"name" : "Antor", "dept": "EEE"}
    ]


    return render(request, "index.html", context={"peoples": peoples})

def about(request):
    return HttpResponse("<h3> <b> BSc. in CSE </b> </h3>")