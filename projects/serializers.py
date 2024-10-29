from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(write_only=True, required=False)

    class Meta:
        model = Project
        fields = '__all__'

    # def validate_email(self, value):
    #     try:
    #         user = User.objects.get(email=value)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("User not found")
        
    #     self.context['user'] = user
    #     return value
