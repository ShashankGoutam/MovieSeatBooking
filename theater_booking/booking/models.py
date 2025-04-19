from django.db import models

class Seat(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    is_booked = models.BooleanField(default=False)  # <- important

    def __str__(self):
        return f"Seat {self.row}-{self.column}"
