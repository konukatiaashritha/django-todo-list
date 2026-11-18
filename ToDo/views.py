from django.shortcuts import render, redirect
from .models import Todo

# Display all tasks
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})


# Add a new task
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Todo.objects.create(
                title=title,
                description=description
            )

        return redirect('todo_list')

    return render(request, 'todo_list.html')


# Mark task as completed
def complete_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.completed = True
        todo.save()

    return redirect('todo_list')


# Delete a task
def delete_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.delete()

    return redirect('todo_list')