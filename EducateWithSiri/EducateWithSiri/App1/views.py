from django.shortcuts import render
from .models import EducationalVideo

# Create your views here.
def index(request):
    return render(request,"App1/index.html")

def home(request):
    videos = EducationalVideo.objects.all()
    return render(request, 'App1/homepage.html', {'videos': videos})

def error(request):
    return render(request,"App1/error.html")