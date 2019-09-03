""" Object checker helper"""

from rest_framework.response import Response
from rest_framework import status

def get_obj_or_404(model, obj_id):
    try:
        obj = model.objects.get(pk=obj_id)
    except model.DoesNotExist:
        message = '{} does not exist'.format(model)
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    return obj
