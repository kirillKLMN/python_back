from rest_framework.serializers import ModelSerializer

from main.models import Command, Task



class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        pass


