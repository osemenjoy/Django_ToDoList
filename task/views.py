from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tasks
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# TaskList view is used to display a list of tasks
class TaskList(LoginRequiredMixin, ListView):
    # Specify the model to use
    model = Tasks
    # Specify the template to use
    template_name = 'task-list.html'
    # Specify the context object name
    context_object_name = 'tasks'

    # Override the get_queryset method to filter tasks by the current user
    def get_queryset(self):
        # Return tasks that belong to the current user
        return Tasks.objects.filter(user=self.request.user)

# TaskCreate view is used to create a new task
class TaskCreate(LoginRequiredMixin, CreateView):
    # Specify the model to use
    model = Tasks
    # Specify the fields to include in the form
    fields = ['title', 'description', 'complete']
    # Specify the template to use
    template_name = 'task-create.html'

    # Override the form_valid method to set the user of the task
    def form_valid(self, form):
        # Set the user of the task to the current user
        form.instance.user = self.request.user
        # Call the parent's form_valid method
        return super().form_valid(form)

# TaskUpdate view is used to update an existing task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    # Specify the model to use
    model = Tasks
    # Specify the fields to include in the form
    fields = ['title', 'description', 'complete']
    # Specify the template to use
    template_name = 'task-update.html'

    # Override the get_object method to check if the task belongs to the current user
    def get_object(self, queryset=None):
        # Get the task object
        obj = super().get_object(queryset=queryset)
        # Check if the task belongs to the current user
        if not obj.user == self.request.user:
            # Raise a 404 error if the task does not belong to the current user
            raise Http404
        # Return the task object
        return obj

# TaskDelete view is used to delete a task
class TaskDelete(LoginRequiredMixin, DeleteView):
    # Specify the model to use
    model = Tasks
    # Specify the template to use
    template_name = 'task-delete.html'
    # Specify the success URL
    success_url = reverse_lazy('tasks')

    # Override the get_object method to check if the task belongs to the current user
    def get_object(self, queryset=None):
        # Get the task object
        obj = super().get_object(queryset=queryset)
        # Check if the task belongs to the current user
        if not obj.user == self.request.user:
            # Raise a 404 error if the task does not belong to the current user
            raise Http404
        # Return the task object
        return obj