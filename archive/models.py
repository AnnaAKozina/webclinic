from django.db import models
import datetime

class Owner(models.Model):
    fname = models.CharField(max_length=250,verbose_name="Имя")
    sname = models.CharField(max_length=250, verbose_name="Фамилия")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    def __str__(self):
        return str(self.id)+" - "+self.sname


class Patient(models.Model):
    name = models.CharField(max_length=250,verbose_name="Кличка")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    species = models.CharField(max_length=50, verbose_name="Вид животного")
    breed = models.CharField(max_length=150, verbose_name="Порода")


    def __str__(self):
        return self.species+" - "+self.name


class Doctor(models.Model):
    fname = models.CharField(max_length=150,verbose_name="Имя")
    sname = models.CharField(max_length=250, verbose_name="Фамилия")
    speciality = models.CharField(max_length=150, verbose_name="Специальность")

    def __str__(self):
        return str(self.id)+" - "+self.sname

class Record(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    rdate = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rdate) +' '+ self.type
