from rest_framework import viewsets  
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def add_tag(self, request, pk=None):
        task = self.get_object()
        tag_id = request.data.get('tag_id')
        
        if not tag_id:
            return Response({'error': 'tag_id is required'}, status=400)
        
        tag = get_object_or_404(Tag, id=tag_id)
        task.tags.add(tag)
        return Response({'status': 'tag added'})

    @action(detail=True, methods=['post'])
    def remove_tag(self, request, pk=None):
        task = self.get_object()
        tag_id = request.data.get('tag_id')
        ф
        if not tag_id:
            return Response({'error': 'tag_id is required'}, status=400)
        
        tag = get_object_or_404(Tag, id=tag_id)
        task.tags.remove(tag)
        return Response({'status': 'tag removed'})

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer