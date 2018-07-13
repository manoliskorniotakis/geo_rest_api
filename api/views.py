from .serializers import MeasurementSerializer, UserSerializer
from .models import Measurements
from .models import Users
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class MeasurementListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = Measurements.objects.filter(id=10)
    serializer_class = MeasurementSerializer


class UserListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

