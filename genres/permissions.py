from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('genres.view_genre')
        return False
