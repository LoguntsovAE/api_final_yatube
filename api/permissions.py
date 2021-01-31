from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True 
        return obj.author == request.user

# опишем что пользователь не может подписаться сам на себя
class AuthorCanNotFollowYourself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author != request.user:
            return True
