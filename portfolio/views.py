from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() #Lista de proyectos
    return render(request, 'home.html', {'projects': projects}) #Reconoce el archivo en la carpeta template