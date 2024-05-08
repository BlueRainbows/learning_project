from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.pagination import PaginationCourse
from materials.serializers.course import CourseSerializer
from materials.services import create_product_course
from materials.tasks import add_mailing_task
from subscription.models import Subscription
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
        course = serializer.save(user=self.request.user)
        product = create_product_course(course.name_course, course.description_course)
        course.product_id = product
        course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        users_list = []
        subscriptions = Subscription.objects.filter(course=course)
        if subscriptions.exists():
            for user in subscriptions:
                users_list.append(user.user.email)
        mailing = add_mailing_task.delay(users_list)
        course.save()
