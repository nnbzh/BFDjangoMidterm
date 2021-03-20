from rest_framework import serializers

from api.models import Book, Journal, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')


class JournalSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField(source='get_type')

    class Meta:
        model = Journal
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
