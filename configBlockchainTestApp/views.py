from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GameData
from datetime import datetime
import time
from .deploy_sepo import deploy_sepo
from asgiref.sync import sync_to_async


async def add_game_data(request):
    start_time = time.time() - 20
    end_time = time.time()
    game_id = "101"
    p1n = "zz"
    p1s = "10"
    p2n = "yy"
    p2s = "15"
    result = game_id + ", " + p1n + p1s + ", " + p2n + p2s
    async_deploy = sync_to_async(deploy_sepo)
    tx_hash = await async_deploy(result)
    # tx_hash = deploy_sepo(result)
    if p1n and p2n and p1s and p2s:
        game_data = GameData(
            game_id= game_id,
            player1_name=p1n,
            player1_points=p1s,
            player2_name=p2n,
            player2_points=p2s,
            game_end_timestamp=datetime.fromtimestamp(time.time()),
            game_duration_secs=end_time - start_time,
            is_tournament_game=False,
            # blockchain_hash="I am test hash olalala",
            blockchain_hash = tx_hash.hex(),
        )
    game_data.save()
    return HttpResponse(f"Result: {game_data.game_id + game_data.blockchain_hash}")
