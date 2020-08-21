from rest_framework import generics
from rest_framework.generics import ListAPIView


from .models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, ListSerializer

class Tree(ListAPIView):
    queryset = Department.objects.filter(parent__isnull=True)
    serializer_class = ListSerializer

class ListDepartment(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ListPosition(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class ListEmployee(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer