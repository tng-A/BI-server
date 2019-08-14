""" Department model """

from django.db import models

from .base import CommonFieldsMixin
from .value_centre import ValueCentre

class Department(CommonFieldsMixin):
    """ Department model e.g Business department"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    value_centre = models.ForeignKey(
        ValueCentre,
        on_delete=models.CASCADE,
        related_name='departments'
    )
