from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerUser, IsSuperUserToRead


class UserView(ListCreateAPIView, PageNumberPagination):
    permission_classes = [IsSuperUserToRead]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewById(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id"
