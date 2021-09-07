from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notebook_app.forms import CreateNoteForm, CreateTodoForm, EditTodoForm, EditNoteForm, UserRegistrationForm
from notebook_app.models import Todo, Note


def create_note(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateNoteForm(request.POST)
            if form.is_valid():
                note = Note(user=request.user, heading=form.cleaned_data['heading'],
                            content=form.cleaned_data['content'])
                note.save()
                print('note created')
                return redirect('notes-page')
        else:
            form = CreateNoteForm()
        context = {'form': form}
        return render(request, 'create_notes.html', context)
    else:
        return redirect('login')


def notes_page(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
        context = {

            'notes': notes
        }
        return render(request, 'notes.html', context)
    else:
        return redirect('login')


def note_detail(request, pk):
    if request.user.is_authenticated:
        note = Note.objects.get(id=pk)
        context = {'note': note}
        return render(request, 'note_detail.html', context)
    else:
        return redirect('login')


def delete_note(request, pk):
    if request.user.is_authenticated:
        note = Note.objects.get(id=pk)
        note.delete()
        return redirect('notes-page')
    else:
        return redirect('login')


def update_note(request, pk):
    if request.user.is_authenticated:
        note = Note.objects.get(id=pk)
        if request.method == "POST":
            form = EditNoteForm(request.POST, instance=note)
            if form.is_valid():
                note.user = request.user
                note.heading = form.cleaned_data['heading']
                note.content = form.cleaned_data['content']
                note.save()
                return redirect('notes-page')
        else:
            form = EditNoteForm(instance=note)

        context = {"form": form}
        return render(request, 'update_note.html', context)
    else:
        return redirect('login')


def todos_page(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

        context = {
            'todos': todos,

        }
        return render(request, 'todos.html', context)
    else:
        return redirect('login')


def create_todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateTodoForm(request.POST)
            if form.is_valid():
                todo = Todo(user=request.user, content=form.cleaned_data['content'])
                todo.save()
                print('todo created')
                return redirect('/todos/')
        else:
            form = CreateTodoForm()
        context = {'form': form}
        return render(request, 'create_notes.html', context)
    else:
        return redirect('login')


def update_todo(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(id=pk)
        if request.method == 'POST':

            form = EditTodoForm(request.POST, instance=todo)
            if form.is_valid():
                todo.user = request.user
                todo.content = form.cleaned_data['content']
                todo.save()
                return redirect('/todos/')
        else:
            form = EditTodoForm(instance=todo)
        context = {'form': form}
    else:
        return redirect('login')

    return render(request, 'update_todo.html', context)


def delete_todo(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos/')
    else:
        return redirect('login')


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration_form.html', context)


def logout(request):
    logout(request)
    return redirect('login')
