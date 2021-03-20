from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet)
router.register(r'journals', viewset=views.JournalViewSet)

urlpatterns = [
    path('', include(router.urls))
]
