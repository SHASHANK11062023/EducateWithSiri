from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"App1/index.html")

def error(request):
    return render(request,"App1/error.html")