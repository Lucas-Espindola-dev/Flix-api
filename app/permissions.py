from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = ''

        return False

    def get_model_permission_codename(self,method, view):
        ...
