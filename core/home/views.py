from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    peoples = [
        {"name" : "Monirul", "dept": "CSE"},
        {"name" : "Akib", "dept": "CSE"},
        {"name" : "Antor", "dept": "EEE"}
    ]

    vegetables = ["Tomatoo", "Pumpkin", "Potatoo", "Ladisfinger"]


    return render(request, "index.html", context={"peoples": peoples, "vegetables": vegetables})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")