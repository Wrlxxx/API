from django_filters import rest_framework as filters
from .models import Task, Tag 

class TaskFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__id',
        queryset=Tag.objects.all(),  
        label='Tags (ID)'
    )

    class Meta:
        model = Task
        fields = ['completed', 'tags']