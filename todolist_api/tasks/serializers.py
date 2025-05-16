from rest_framework import serializers
from .models import Task, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        source='tags',
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'tags', 'tag_ids']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        task = Task.objects.create(**validated_data)
        task.tags.set(tags_data)
        return task

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            instance.tags.set(tags_data)
        return super().update(instance, validated_data)