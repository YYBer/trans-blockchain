from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GameData
from datetime import datetime
from .deploy_sepo import tx_hash
# from deploy_sepo import tx_hash
import time
import random

def add_game_data(request):
    start_time = time.time() - 20
    end_time = time.time()
    gameid = random.randint(0, 10000)
    p1n = "zz"
    p1s = "10"
    p2n = "yy"
    p2s = "15"
    game_result = str(gameid) + ", " + p1n + p1s + ", " + p2n + p2s
    hash = tx_hash.hex()
    print("olalala")
    # print(f'Contact transaction hash in views {tx_hash.hex()}')
    if p1n and p2n and p1s and p2s:
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
            blockchain_hash=hash,
        )
    game_data.save()
    return HttpResponse(f"Result: {game_result + hash}")



