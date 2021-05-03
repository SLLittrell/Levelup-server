from django.db import models

class GameCategory(models.Model):
    label = models.CharField(max_length=55)