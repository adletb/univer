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

class PositionSerializer(serializers.ModelSerializer):
    first = serializers.StringRelatedField()
    class Meta:
        model = Position
        fields = ['id', 'position', 'stavka', 'department', 'first']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_n', 'middle_n', 'last_n', 'code', 'foto', 'position_one', 'position_two']

