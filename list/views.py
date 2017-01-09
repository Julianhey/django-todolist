from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Todo, Comment, GameInstance
from .forms import TodoForm, CommentForm, GameForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from registration.backends.simple.views import RegistrationView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GameSerializer


# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(
        deadline_date__lte=timezone.now()).order_by('deadline_date')
    return render(request, 'list/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'list/todo_detail.html', {'todo': todo})

@login_required
def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'list/todo_edit.html', {'form': form})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'list/todo_edit.html', {'form': form})

@login_required
def todo_remove(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')

def add_comment_to_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.todo = todo
            comment.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = CommentForm()
    return render(request, 'list/add_comment_to_todo.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('todo_detail', pk=comment.todo.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    todo_pk = comment.todo.pk
    comment.delete()
    return redirect('todo_detail', pk=todo_pk)


class GameLibraryView(LoginRequiredMixin, generic.ListView):
    model = GameInstance
    template_name = 'list/gameinstance_list_user.html'


    def get_queryset(self):
        return GameInstance.objects.filter(user=self.request.user)

@login_required
def game_add(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            gameinstance = form.save(commit=False)
            gameinstance.user = request.user
            gameinstance.save()
            return redirect('my-library')
    else:
            form = GameForm()
            return render(request, 'list/game_add.html', {'form': form})



class GameList(APIView):
    def get(self, request):
        games = GameInstance.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self):
        pass
