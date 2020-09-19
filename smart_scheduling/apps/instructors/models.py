from django.db import models

from multiselectfield import MultiSelectField


class Instructor(models.Model):

    HOUR_CHOICES = [
        (1, '1 Jam '),
        (2, '2 Jam'),
        (3, '3 Jam'),
    ]

    DAYS_CHOICES = (
        (1, 'Senin'),
        (2, 'Selasa'),
        (3, 'Rabu'),
        (4, 'Kamis'),
        (5, 'Jumat'),
        (6, 'Sabtu')
    )

    name = models.CharField(max_length=250)
    hour = models.IntegerField(choices=HOUR_CHOICES)
    days = MultiSelectField(choices=DAYS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
