from rest_framework import permissions


class PermissionModer(permissions.BasePermission):
    message = 'Недостаточно прав.'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator_course_and_lesson').exists():
            return True
        else:
            return False


class PermissionUser(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
