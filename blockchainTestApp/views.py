from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GameData
from datetime import datetime
import time


def add_game_data(request, p1n, p1s, p2n, p2s):
    print(f"Incoming arguments: p1n={p1n}, p2n={p2n}, p1s={p1s}, p2s={p2s}")
    start_time = time.time() - 20
    end_time = time.time()
    if p1n and p2n and p1s and p2s:
        game_data = GameData(
            player1_name=p1n,
            player1_points=p1s,
            player2_name=p2n,
            player2_points=p2s,
            game_end_timestamp=datetime.fromtimestamp(time.time()),
            game_duration_secs=end_time - start_time,
            is_tournament_game=False,
            blockchain_hash=None
            # game_ID=game_data.id
        )
        game_data.save()
        return HttpResponse(f"Record ID: {game_data.id}")
def result ():
     _msg = "hello"
     return _msg

def add_hash_data_test(request):
    from blockchainTestApp.deploy_sepo import tx_hash
    print(f"request= {request}")
    # print(f"Incoming argument: hash={hash}")
    #if hash:
    game_data = GameData(
        player1_name = 'aaa',
        player1_points = 22,
        player2_name = 'bbb',
        player2_points = 33,
        game_end_timestamp = datetime.fromtimestamp(time.time()),
        game_duration_secs = 20,
        is_tournament_game = False,
        # result = player1_name+player1_points+' '+player2_name+player2_points,
        blockchain_hash = tx_hash.hex()
    )
    game_data.save()
    return HttpResponse(f"Record ID: {game_data.id}, record hash: {game_data.blockchain_hash}")
    
def get_game_by_id(id_value):
    try:
            obj = GameData.objects.get(id = id_value)
            return obj
    except GameData.DoesNotExist:
            return None

def add_hash_data(request, id_value, hash):
    print(f"Incoming argument: hash={hash}")
    if id_value:
        obj = get_game_by_id(id_value)
        if obj:
            obj.hash = hash
            obj.save()
            return HttpResponse(f"Record hash: {obj.hash}")
    return HttpResponse(f"Record not found or hash not added")

# def my_view_end_game(request):
#      if request.method == 'POST':
#           new_obj = add_game_data()