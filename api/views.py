from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from .models import User, Post
from .serializers import UserSerializer, UserRegistrationSerializer, PostSerializer
from rest_framework import status
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Post
from .serializers import UserProfileSerializer, PostSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class UserLoginAPIView(ObtainJSONWebToken):
    pass

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class UserProfileView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(author__username=username)

class UserFollowersView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        user = UserProfile.objects.get(username=username)
        return user.followers.all()

class UserFollowingView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        user = UserProfile.objects.get(username=username)
        return user.following.all()