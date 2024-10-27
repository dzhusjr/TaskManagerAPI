from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from tasks.models import Task
from projects.models import Project
from users.models import User
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def by_project(self, request):
        project_id = request.query_params.get('project_id')
        email = request.query_params.get('email')

        if not project_id or not email:
            return Response(
                {'error': 'Both project_id and email parameters are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            project = Project.objects.get(pk=project_id)
            user = User.objects.get(email=email)

            if not project.users.filter(id=user.id).exists():
                return Response(
                    {'error': f'User {user.username} not assigned to {project.title} project.'},
                    status=status.HTTP_403_FORBIDDEN
                )

            tasks = Task.objects.filter(project=project)

            page = self.paginate_queryset(tasks)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)

        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
