from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from api import views

router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet)
router.register(r'journals', viewset=views.JournalViewSet)
router.register(r'auth', viewset=views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', obtain_jwt_token)
]
