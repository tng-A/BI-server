from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


from src.api.serializers.user import (
    RegistrationSerializer,
    LoginSerializer
)
from src.api.models import Company


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RegistrationSerializer


class LoginGenericAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
