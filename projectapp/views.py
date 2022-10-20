from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 10