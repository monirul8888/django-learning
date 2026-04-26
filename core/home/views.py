from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("<h3> <b> BSc. in CSE </b> </h3>")