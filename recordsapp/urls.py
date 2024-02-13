from django.urls import path

from recordsapp.views import (edit_vaccine, new_vaccine, new_vaccine_delivery,
                              vaccinate_patient, vaccinations, vaccines)

urlpatterns = [
    path("vaccines/", vaccines, name="vaccines"),
    path("new-vaccine/", new_vaccine, name="new-vaccine"),
    path("edit-vaccine/", edit_vaccine, name="edit-vaccine"),
    path("new-delivery/", new_vaccine_delivery, name="new-delivery"),
    path("vaccinations/", vaccinations, name="vaccinations"),
    path("vaccinate-patient/", vaccinate_patient, name="vaccinate-patient"),
]