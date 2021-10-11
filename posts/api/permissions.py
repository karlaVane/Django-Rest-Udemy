from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly (BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or 'POST':
            return True
        else:
            return request.user.is_staff #el usuario es tipo staff

            
