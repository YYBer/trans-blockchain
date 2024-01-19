from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import GameData
from datetime import datetime
import time
import random
import os

def get_game_result():
    # gameid = random.randint(0, 9999)
    gameid = 99
    p1n = "zz"
    p1s = "10"
    p2n = "yy"
    p2s = "15"
    game_result = game_result = str(gameid) + ", " + p1n + p1s + ", " + p2n + p2s
    return game_result

def add_game_data(request):
    start_time = time.time() - 20
    end_time = time.time()
    game_result = get_game_result()
    gameid = int(game_result[:2])
    p1n = "zz"
    p1s = "10"
    p2n = "yy"
    p2s = "15"
    if p1n and p2n and p1s and p2s:
        from .deploy_sepo import tx_hash
        game_data = GameData(
            game_id=gameid,
            player1_name=p1n,
            player1_points=p1s,
            player2_name=p2n,
            player2_points=p2s,
            game_end_timestamp=datetime.fromtimestamp(time.time()),
            game_duration_secs=end_time - start_time,
            is_tournament_game=False,
            # blockchain_hash=game_result,
            blockchain_hash = tx_hash.hex(),
        )
    game_data.save()
    return HttpResponse(f"Result: {game_result + game_data.blockchain_hash}")

    


# def add_game_data(request):
#     start_time = time.time() - 20
#     end_time = time.time()
#     gameid = random.randint(0, 9999)
#     p1n = "zz"
#     p1s = "10"
#     p2n = "yy"
#     p2s = "15"
#     game_result = str(gameid) + ", " + p1n + p1s + ", " + p2n + p2s
#     print('hooooo')
#     if p1n and p2n and p1s and p2s:
#         # from .deploy_sepo import tx_hash
#         game_data = GameData(
#             game_id=gameid,
#             player1_name=p1n,
#             player1_points=p1s,
#             player2_name=p2n,
#             player2_points=p2s,
#             game_end_timestamp=datetime.fromtimestamp(time.time()),
#             game_duration_secs=end_time - start_time,
#             is_tournament_game=False,
#             blockchain_hash=game_result,
#             # blockchain_hash = tx_hash.hex(),
#         )
#     game_data.save()
#     return HttpResponse(f"Result: {game_result + game_data.blockchain_hash}")