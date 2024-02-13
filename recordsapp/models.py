from django.db import models

from core.models import AbstractBaseModel


# Create your models here.
class Vaccine(AbstractBaseModel):
    name = models.CharField(max_length=500)
    company = models.CharField(max_length=255)
    dosage_per_immunization = models.CharField(max_length=255)
    description = models.TextField(null=True)
    quantity = models.FloatField(default=0)
    on_hold = models.FloatField(default=0)

    def __str__(self):
        return self.name


class VaccineDelivery(AbstractBaseModel):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    amount_delivered = models.FloatField(default=0)

    def __str__(self):
        return self.vaccine.name


class VaccinationRecord(AbstractBaseModel):
    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name="patientvaccinations")
    nurse = models.ForeignKey("users.Nurse", on_delete=models.SET_NULL, null=True, related_name="nursevaccinations")
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True)
    vaccine_schedule = models.ForeignKey("appointments.VaccineSchedule", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.patient.first_name} has been vaccinated with {self.vaccine.name}"