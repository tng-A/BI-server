""" Period Model"""

from django.db import models
from .company import Company

class Period(models.Model):
    PERIOD_TYPES = (
        ('quarterly', 'Quaterly'),
        ('monthly', 'Monthly'),
    )
    YEARS = (
        ('2019', '2019'),
        ('2020', '2020')
    )
    name = models.CharField(max_length=255, null=False)
    year = models.CharField(
        max_length=30,
        choices=YEARS,
        default='2019',
        db_index=True
    )
    period_type = models.CharField(
        max_length=30,
        choices=PERIOD_TYPES, db_index=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='periods'
    )

    def __str__(self):
        return self.name
