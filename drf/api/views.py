from myapp.models import Student
from employee.models import Employee
from .serializers import StudentSerializer,EmployeeSerializer,blogSerializer,commentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from blog.models import blog,comment
from rest_framework import mixins
from rest_framework import generics 
import django_filters.rest_framework
from rest_framework import viewsets
from employee.filters import EmployeeFilter

@api_view(['GET','POST'])
def studentAPI(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])     
def studentIDAPI(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#class based views
'''class EmployeeView(APIView):
    def get(self,request):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)'''

'''
#Mmixin
class EmployeeView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
'''
'''
#Generics
class EmployeeView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
'''
'''
#viewsets
class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
        
#model viewsets
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'
    filterset_class = EmployeeFilter

class blogAPI(generics.ListCreateAPIView):
    queryset=blog.objects.all()
    serializer_class=blogSerializer
class commentapi(generics.ListCreateAPIView):
    queryset=comment.objects.all()
    serializer_class=commentSerializer