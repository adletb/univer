from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey('Position', null=True, blank=True, related_name="director", on_delete=models.SET_NULL)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Position(models.Model):
    position = models.CharField(max_length=100)
    stavka = models.PositiveIntegerField(default=0)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
        return self.position


class Employee(models.Model):
    first_n = models.CharField(max_length=20)
    middle_n = models.CharField(max_length=20, blank=True)
    last_n = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField(default=0)
    foto = models.ImageField(upload_to="foto/", null=True, blank=True)
    position_one = models.ForeignKey('Position', null=True, on_delete=models.SET_NULL, related_name="first")
    position_two = models.ForeignKey('Position', null=True, blank=True, on_delete=models.SET_NULL, related_name="second")

    def __str__(self):
        return f"{self.last_n} {self.first_n} {self.middle_n}"