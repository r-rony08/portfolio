from django.shortcuts import render
from .models import Project

from django.shortcuts import redirect
from .forms import ProjectForm

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {'form': form})

