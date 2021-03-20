from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import Book, Journal
from api.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
