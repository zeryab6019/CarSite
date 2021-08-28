from django.shortcuts import render
from .models import Team
# Create your views here.
def Index(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }

    return render(request, 'appPages/index.html',data)

def Cars(request):
    return render(request, 'appPages/cars.html')

def About(request):
    team_members = Team.objects.all()
    fata = {
        'leams':team_members
    }
    return render(request, 'appPages/about.html', fata)

def Services(request):
    return render(request, 'appPages/services.html')

def Contact(request):
    return render(request, 'appPages/contact.html')

def Search(request):
    return render(request, 'appPages/search.html')
