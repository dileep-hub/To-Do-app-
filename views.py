from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import*

# Create your views here.
def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks' : tasks, 'form' : form}   # context is very important here as it is thing appears on the template
	return render(request, 'tasks/list.html', context)  

def updateTask(request, pk):     # here pk is primary key
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task) # here instance=task because u need form of only one task

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid:
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item' : item}
	return render(request, 'tasks/delete.html', context)