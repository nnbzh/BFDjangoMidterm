import json

from django.http import JsonResponse
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_jwt.views import obtain_jwt_token

from api.models import Book, Journal, User
from api.serializers import BookSerializer, JournalSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #
    # @action(detail=False, methods=['POST'], url_path='login')
    # def login(self):
    #     return obtain_jwt_token

    @action(detail=False, methods=['POST'], url_path='register')
    def register(self, request):
        data = request.data
        new = User.objects.create_user(data['email'], data['password'])
        serializer = self.get_serializer()
        return JsonResponse(serializer.data(new), safe=False)
