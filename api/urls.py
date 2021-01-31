from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import include 
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet


router = DefaultRouter() 
router.register('posts', PostViewSet, basename='post') 
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register('group', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]