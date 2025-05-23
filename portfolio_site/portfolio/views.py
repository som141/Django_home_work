from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Rating

def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})

def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/detail.html', {'project': project})

def rate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        score = int(request.POST['score'])
        Rating.objects.create(project=project, score=score)
    return redirect('portfolio:detail', pk=pk)

