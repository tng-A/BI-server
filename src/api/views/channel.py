""" Channel views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from src.api.serializers.channel import ChannelSerializer
from src.api.models import Channel

class ChannelListCreateAPIView(ListCreateAPIView):
    """ Get/Create channels of payment"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
