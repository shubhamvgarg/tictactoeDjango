from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')
        print("testing view")
        print(username)
        print(option)
        print(room_code)
        if option == '1':
            game = Game.objects.filter(room_code=room_code).first()

            if game is None:
                messages.success(request, 'Room Code Not Found')
                return redirect('/')
            
            if game.is_over:
                messages.success(request, 'Game Over')
                return redirect('/')

            game.game_opponent = username
            game.save()
            return redirect(f'/play/{room_code}?username={username}')

        
        if option == '2':
            game=Game(game_creator = username, room_code=room_code)
            game.save()
            return redirect(f'/play/{room_code}?username={username}')
            

    return render(request, 'home.html')

def play(request, room_code):
    username = request.GET.get('username')
    context = {'room_code': room_code, 'username': username}

    return render(request, 'play.html', context)