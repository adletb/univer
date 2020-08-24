from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey('Position', null=True, blank=True, related_name="director", on_delete=models.SET_NULL)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

def number_employee(value):
    number_employeers = len(list(Position.objects.filter(employee=value)))
    if number_employeers > 1 :
        raise ValidationError(
            _('%(value)s уже на двух должностях'),
            params={'value': value}
        )

class Position(models.Model):
    name = models.CharField( max_length=100)
    code = models.PositiveSmallIntegerField(default=0)
    stavka = models.PositiveIntegerField(default=0)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='positions')
    employee = models.ForeignKey('Employee', validators=[number_employee], null=True,  on_delete=models.SET_NULL, related_name='employee')
    def __str__(self):
        return f"{self.name} {self.employee}"


class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True, default='')
    foto = models.ImageField(upload_to="foto/", null=True, blank=True)

    def __str__(self):
        return self.name