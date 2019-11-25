from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404
from rest_framework import authentication, permissions, generics
# from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User, UserManager

# Create your views here.

# 사용자 Create View(POST)
class UserInfoCreate(generics.CreateAPIView):
    permission_classes =(permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 사용자 정보 Detail(Read) View(GET)
class UserInfoDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        return Response(data={
            'username' : request.user.username,
            'email' : request.user.email,
            'profile' : request.user.profile,
        },
        status = status.HTTP_200_OK)

# 사용자 정보 Update View(PUT)
class UserInfoUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.pk)
            return instance
        except User.DoesNotExist:
            raise Http404

# 사용자 정보 Delete View(PUT)
class UserInfoDelete(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.pk)
            return instance
        except User.DoesNotExist:
            raise Http404