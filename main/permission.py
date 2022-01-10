from rest_framework.permissions import BasePermission


class IsAdAuthor(BasePermission):

    def has_oblect_permission(self, request, view, obj):
            return request.user.is_authenticated and request.user == obj.author