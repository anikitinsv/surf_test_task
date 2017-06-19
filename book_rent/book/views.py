from rest_framework import serializers, generics
from book.models import Book
from book_author.models import BookAuthor
from user.models import RentUser
from rest_framework.response import Response
import datetime
# Create your views here.

# Serializers define the API representation.

class BookAuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False, max_length=128)
    second_name = serializers.CharField(required=False, max_length=128)
    surname = serializers.CharField(required=False, max_length=128)


    class Meta:
        model = BookAuthor
        fields = ('id','first_name', 'second_name', 'surname')

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = BookAuthorSerializer(many=True, read_only=True)
    book_name = serializers.CharField(required=False, max_length=256)
    rent_cost = serializers.FloatField(required=False)
    count_month_rented = serializers.IntegerField()
    rent_estimate_time = serializers.DateTimeField(required=False)
    owner = serializers.PrimaryKeyRelatedField(queryset=RentUser.objects.all(), required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.rent_cost = validated_data.get('language', instance.rent_cost)
        instance.count_month_rented = validated_data.get('count_month_rented', instance.count_month_rented)
        instance.owner = validated_data.get('owner', instance.owner)
        # Take money
        user = instance.owner
        if user.money < instance.rent_cost * instance.count_month_rented:
            raise serializers.ValidationError('Need more money')
        user.money -= instance.rent_cost * instance.count_month_rented
        user.save()
        instance.save()
        return instance

# View for address /books/
# View all renting books for user
class BookListView(generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all().filter(owner__id=request.user.id, rent_estimate_time__gte=datetime.datetime.now())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, headers={'Token': request.auth.key})

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# View for address /books/<book_id>
# Allow GET, PUT, POST, PATCH, HEAD, OPTIONS
class BookViewDetail(BookListView):

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk', 0)
        queryset = self.get_queryset().filter(pk=pk, owner__id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, headers={'Token': request.auth.key})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not request.data.get('owner', None):
            request.data['owner'] = request.user.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        ret = serializer.data

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(ret)
