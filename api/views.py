from rest_framework import viewsets 
from rest_framework.generics import get_object_or_404 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from django_filters import rest_framework as filters 
from .models import Comment, Follow, Group, Post, User 
from .permissions import IsAuthorOrReadOnlyPermission, AuthorCanNotFollowYourself
from .serializers import CommentSerializer, PostSerializer, GroupSerializer, FollowSerializer

class CommentViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission] 
 
    def get_queryset(self): 
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id')) 
        return post.comments.all() 
 
    def perform_create(self, serializer): 
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id')) 
        serializer.save(author=self.request.user, post_id=post.id)

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [IsAuthorOrReadOnlyPermission, IsAuthenticated]
 
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet): 
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer 
    # permission_classes = [IsAuthorOrReadOnlyPermission, IsAuthenticated]


class FollowViewSet(viewsets.ModelViewSet): 
    # затереть строку, переписать юрл
    queryset = Follow.objects.all() 
    serializer_class = FollowSerializer 
    permission_classes = [AuthorCanNotFollowYourself, IsAuthenticated]
    # filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', ]
    
    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer): 
        serializer.save(follower=self.request.user)
