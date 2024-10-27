from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Project
from tasks.models import Task
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['post'])
    def add_user(self, request, pk=None):
        try:
            project = self.get_object()
            email = request.data.get('email')

            if not email:
                return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            if user in project.users.all():
                return Response({'error': 'User is already added to this project'}, status=status.HTTP_400_BAD_REQUEST)

            if project.users.count() >= 3:
                return Response({'error': 'This project already has 3 users'}, status=status.HTTP_400_BAD_REQUEST)

            project.users.add(user)

            return Response({'message': 'User added successfully to the project'}, status=status.HTTP_200_OK)

        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['post'])
    def add_task(self, request, pk=None):
        try:
            project = self.get_object()
            task_id = request.data.get('task_id')

            if not task_id:
                return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

            if task.project is not None:
                return Response({'error': 'Task is already assigned to a project'}, status=status.HTTP_400_BAD_REQUEST)

            task.project = project
            task.save()

            return Response({'message': 'Task added successfully to the project'}, status=status.HTTP_200_OK)

        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
