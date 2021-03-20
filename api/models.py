from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from api.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    class Type(Enum):
        BULLET = "BULLET"
        FOOD = "FOOD"
        TRAVEL = "TRAVEL"
        SPORT = "SPORT"

        def to_representation(self, obj):
            if obj == '' and self.allow_blank:
                return obj
            return self._choices[obj]

    type = models.CharField(max_length=255, choices=[(tag, tag.value) for tag in Type])
    publisher = models.CharField(max_length=255)
