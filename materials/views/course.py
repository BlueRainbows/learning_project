from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.pagination import PaginationCourse
from materials.serializers.course import CourseSerializer
from users.permissions import PermissionModer, PermissionUser


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = PaginationCourse

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~PermissionModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (PermissionModer | PermissionUser,)
        elif self.action == 'destroy':
            self.permission_classes = (~PermissionModer | PermissionUser,)
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(user=self.request.user)
        user.save()
