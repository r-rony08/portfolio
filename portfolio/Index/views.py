from django.shortcuts import render
from .models import Project

from django.shortcuts import redirect
from .forms import ProjectForm

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    project_list = Project.objects.all().order_by('-id') 
    paginator = Paginator(project_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})
  
@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
