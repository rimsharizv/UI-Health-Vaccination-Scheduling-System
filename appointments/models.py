from django.db import models

from core.models import AbstractBaseModel


# Create your models here.
class VaccineSchedule(AbstractBaseModel):
    vaccine = models.ForeignKey("recordsapp.Vaccine", on_delete=models.SET_NULL, null=True)
    session_date = models.DateField()
    capacity = models.IntegerField(default=100)
    occupied_slots = models.IntegerField(default=0)
    available_slots = models.IntegerField(default=100)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.vaccine.name} - {self.session_date}"


class Appointment(AbstractBaseModel):
    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name="patientappointments")
    nurse = models.ForeignKey("users.Nurse", on_delete=models.SET_NULL, null=True, related_name="nurseappointments")
    session = models.ForeignKey(VaccineSchedule, on_delete=models.SET_NULL, null=True)
    #vaccine = models.ForeignKey("recordsapp.Vaccine", on_delete=models.SET_NULL, null=True)
    accepted = models.CharField(max_length=255, default="Pending")
    

    def __str__(self):
        return str(self.id)


class NurseSchedule(AbstractBaseModel):
    nurse = models.ForeignKey("users.Nurse", on_delete=models.CASCADE, related_name="nurseschedules")
    vaccine_schedule = models.ForeignKey(VaccineSchedule, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, default="Pending")

    def __str__(self):
        return self.nurse.user.name