from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    category = models.ForeignKey("GameCategory", on_delete=models.CASCADE)
    skill_level = models.IntegerField()
