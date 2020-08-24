from django.urls import path
from .views import ListDepartment, DepartmentDetail, Tree, ListEmployee, EmployeeDetail, ListPosition, PositionDetail

app_name = "univer"

urlpatterns = [
    path('departaments', ListDepartment().as_view()),
    path('employee', ListEmployee().as_view()),
    path('positions', ListPosition().as_view()),
    path('departament/<int:pk>', DepartmentDetail().as_view()),
    path('employee/<int:pk>', EmployeeDetail().as_view()),
    path('position/<int:pk>', PositionDetail().as_view()),
    path('tree/', Tree().as_view())
]