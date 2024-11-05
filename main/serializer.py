from rest_framework.serializers import ModelSerializer

from main.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

