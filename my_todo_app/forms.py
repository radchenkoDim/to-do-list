from django import forms
from .models import Task


class TaskForm(forms.Form):
    task = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    def clean_task(self):
        task = self.cleaned_data['task']

        if Task.objects.filter(title=task).exists():
            raise forms.ValidationError(f'Task with the name "{task}" already exists.')
        if len(task) < 3:
            raise forms.ValidationError('Task must be at least 3 characters long.')

        return task
    

class DeleteTaskForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.HiddenInput())
    
    def clean_task_id(self):
        task_id = self.cleaned_data['task_id']
        task = Task.objects.filter(id=task_id).first()

        if task is None:
            raise forms.ValidationError(f'Task with id "{task_id}" does not exist.')
            
        return task_id