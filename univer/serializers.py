from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Department, Position, Employee

class ListSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    children = RecursiveField(many=True)
    positions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'director', 'children', 'positions']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'director', 'parent']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [ 'id', 'name', 'foto']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'id', 'code', 'stavka', 'department', 'employee']


