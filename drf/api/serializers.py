from rest_framework import serializers
from myapp.models import Student
from employee.models import Employee
from blog.models import blog,comment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= '__all__'
        
        
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
class blogSerializer(serializers.ModelSerializer):
    comments=commentSerializer(many=True,read_only=True)
    class Meta:
        model=blog
        fields='__all__'
