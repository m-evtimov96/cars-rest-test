from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.models import Token

from .permissions import IsProfileOwnerOrReadOnly
from .models import User
from .serializers import UserSerializer, RegistrationSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsProfileOwnerOrReadOnly]


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        req_data = {}
        if serializer.is_valid():
            account = serializer.save()
            req_data['response'] = 'successful registration'
            req_data['username'] = account.username
            req_data['email'] = account.email
            req_data['token'] = Token.objects.get(user=account).key
            req_status = status.HTTP_201_CREATED
        else:
            req_data = serializer.errors
            req_status = status.HTTP_400_BAD_REQUEST
        return Response(data=req_data, status=req_status)
