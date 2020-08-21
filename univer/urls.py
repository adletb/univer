from django.urls import path
from .views import ListDepartment, ListPosition, ListEmployee, DepartmentDetail, PositionDetail, EmployeeDetail, Tree

app_name = "univer"

urlpatterns = [
    path('departs', ListDepartment().as_view()),
    path('departs/<int:pk>', DepartmentDetail().as_view()),
    path('positions/', ListPosition().as_view()),
    path('positions/<int:pk>', PositionDetail.as_view()),
    path('employees/', ListEmployee().as_view()),
    path('employees/<int:pk>', EmployeeDetail.as_view()),
    path('tree/', Tree().as_view())
]