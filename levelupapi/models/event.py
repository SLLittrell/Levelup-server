from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    location = models.CharField(default= "null", max_length=100)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees =models.ManyToManyField("Gamer", through="Attendee", related_name="attending")