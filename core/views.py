from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
import datetime

# from .forms import CommandForm


from django.http import HttpResponse
from .models import User, Command


def index(request):

    return render(request, "core/home.html")


def render_user(request, user_id):
    user = User.objects.get(id=user_id)
    data = {"user": user}
    return render(request, "core/details.html", data)


def all_users(request):
    users = User.objects.all()

    context = {"users": users}
    return render(request, "core/users.html", context)


def list_commands(request, user_id):
    user = User.objects.get(pk=user_id)
    print(user)
    commands = Command.objects.filter(creator=user)
    print(commands)
    context = {"commands": commands}
    return render(request, "core/commands.html", context)


def get_commands(request):
    commands = Command.objects.all()
    context = {"commands": commands}
    return render(request, "core/commands.html", context)


def delete_command(request, command_id):
    command = Command.objects.get(id=command_id)
    print(command)
    try:
        command.delete()
    except Exception as e:
        print("exception occurred in deleting command as ", e)
    return redirect(get_commands)


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    print(user)
    try:
        user.delete()
    except Exception as e:
        print("exception deleting user: ", e)
    return redirect(all_users)


def update_command_page(request, command_id):
    command = Command.objects.get(id=command_id)
    print(command)
    print(command.id)
    print(command.command_text)
    context = {"command": command}

    return render(request, "core/update_command.html", context)


def update_command(request):

    if request.method == "POST":
        command_id = request.POST["commandId"]
        command_text_new = request.POST["commandTextNew"]
        command = Command.objects.get(id=command_id)
        command.command_text = command_text_new
        command.save()

    return redirect(get_commands)


def add_command(request):
    if request.method == "POST":
        print("post method")
        for key, value in request.POST.items():
            print(key, value)
        creator = User.objects.get(id=request.POST["userId"])
        # d = datetime(2015, 10, 09, 23, 55, 59, 342380)
        d = datetime.datetime.now()
        cmd_new = Command.objects.create(
            creator=creator, command_text=request.POST["commandTextNew"],added_at=d
        )
        print(cmd_new)
    return redirect(get_commands)


def add_command_page(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "core/add_command_page.html", context)
