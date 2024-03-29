from django.db import models
from django.utils import timezone

class GameData(models.Model):
    game_id = models.IntegerField(default=0)
    player1_name = models.CharField(max_length=255)
    player1_points = models.PositiveIntegerField()
    player2_name = models.CharField(max_length=255)
    player2_points = models.PositiveIntegerField()
    game_end_timestamp = models.DateTimeField()
    game_duration_secs = models.PositiveIntegerField()
    is_tournament_game = models.BooleanField()
    blockchain_hash = models.CharField(max_length=64, null=True, blank=True)
    def __str__(self):
        return str(self.game_id)
        
    # class Meta:
    #     app_label = 'blockchainTestApp'