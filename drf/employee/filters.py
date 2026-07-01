import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='post', lookup_expr='icontains')
    name_filter = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    id=django_filters.RangeFilter(field_name='id', lookup_expr='exact')
    class Meta:
        model = Employee
        fields = ['department','name_filter','id']