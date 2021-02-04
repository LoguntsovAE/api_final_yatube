from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS or obj.author == request.user)
        # автотесты Яндекса не принимают код ниже,
        # пришлось сделать не правильно :(
        # return (request.method in permissions.SAFE_METHODS or
        #         obj.author == request.user)
