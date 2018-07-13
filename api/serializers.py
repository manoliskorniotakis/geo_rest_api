from rest_framework.serializers import ModelSerializer
from .models import Measurements
from .models import Users


class MeasurementSerializer(ModelSerializer):

    class Meta:
        model = Measurements
        fields = ('id', 'network_type', 'lon', 'lat', 'lac')


class UserSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'email', 'username', 'password')

'''
    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            password=validated_data['password'])
        user.save()
        return user
'''