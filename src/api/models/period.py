""" Period Model"""

from django.db import models


class Period(models.Model):
    PERIOD_TYPES = (
        ('yearly', 'Yearly'),
        ('halfyearly', 'Half Yearly'),
        ('quarterly', 'Quaterly'),
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
        ('daily', 'Daily'),
    )
    start = models.DateField()
    end = models.DateField()
    period_type = models.CharField(
        max_length=30,
        choices=PERIOD_TYPES, db_index=True)

    def __str__(self):
        return self.period_type
