from rest_framework.viewsets import ModelViewSet 
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .models import Todo
from .serializers import TodoModelSerializer, UserModelSerializer
from .permissions import IsAdminOrIsAuthReadOnly

# Create your views here.
class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    
    def update(self, request, *args, **kwargs):
        todo_pk = kwargs['pk']
        todo_row = Todo.objects.get(pk=todo_pk)
        if todo_row.user.pk == request.user.pk or request.user.is_staff:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            raise PermissionDenied


    def destroy(self, request, *args, **kwargs):
        todo_pk = kwargs['pk']
        todo_row = Todo.objects.get(pk=todo_pk)
        if todo_row.user.pk == request.user.pk or request.user.is_staff:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAdminOrIsAuthReadOnly,)

