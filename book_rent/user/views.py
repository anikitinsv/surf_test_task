from rest_framework import serializers
from user.models import RentUser
from rest_framework import generics
from rest_framework.response import Response


class RentUserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    login = serializers.PrimaryKeyRelatedField(read_only=True)
    money = serializers.FloatField(required=False)
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return RentUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.login = validated_data.get('login', instance.login)
        instance.money = validated_data.get('money', instance.money)
        instance.save()
        return instance


# Address /users/
class RentUserList(generics.ListAPIView):
    queryset = RentUser.objects.all()
    serializer_class = RentUserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(login=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, headers={'Token': request.auth.key})

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Address /users/<user_id>
class RentUserDetail(RentUserList, generics.UpdateAPIView):
    queryset = RentUser.objects.all()
    serializer_class = RentUserSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
