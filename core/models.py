from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField()
    has_projector = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#class Reservation(models.Model):

