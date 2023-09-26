from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, PostCreateAPIView,  UserProfileView, UserPostsView, UserFollowersView, UserFollowingView



urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<str:username>/posts/', UserPostsView.as_view(), name='user-posts'),
    path('profile/<str:username>/followers/', UserFollowersView.as_view(), name='user-followers'),
    path('profile/<str:username>/following/', UserFollowingView.as_view(), name='user-following'),
]

