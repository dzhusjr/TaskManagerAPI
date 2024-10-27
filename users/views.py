from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()

        password = request.data.get('password')

        if not password:
            return Response({'error': 'Password is required to delete the user.'}, status=status.HTTP_400_BAD_REQUEST)

        # if check_password(password, user.password):
        if password == user.password:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'error': 'Incorrect password'}, status=status.HTTP_403_FORBIDDEN)
