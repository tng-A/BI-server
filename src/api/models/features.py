""" Feature model """

from django.db import models
from django.contrib.auth.models import Group

from .base import CommonFieldsMixin
from .user import User

class Feature(CommonFieldsMixin):
    """ Feature model e.g graph """
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class FeaturePermissions(CommonFieldsMixin):
    """ Define feature permissions"""
    feature = models.OneToOneField(
        Feature,
        on_delete=models.CASCADE,
        related_name='features',
    )
    group = models.ManyToManyField(
        Group,
        related_name='groups',
    )
    def __str__(self):
        return '{}'.format(self.feature.name)


class EnabledFeature(CommonFieldsMixin):
    """ Define enabled features"""
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        related_name='enabled_features',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
    )
    is_enabled = models.BooleanField(
        default=True
    )
    def __str__(self):
        return '{}'.format(self.feature.name)

