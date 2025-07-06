from django.shortcuts import render
from .models import Project

from django.shortcuts import redirect
from .forms import ProjectForm

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

