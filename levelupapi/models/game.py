from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    min_players = models.CharField(max_length=3)
    max_players = models.CharField(max_length=3)
    category = models.ForeignKey("GameCategory", on_delete=models.CASCADE)
