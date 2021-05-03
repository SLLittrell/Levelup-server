from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)