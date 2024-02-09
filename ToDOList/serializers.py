from rest_framework import serializers

from ToDOList.models import TodoList

from . import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TodoList
        fields = ('id', 'title','description', 'completed', 'created_at')
