from django.urls import path

from users.views import (admin_edit_nurse, create_patient, delete_nurse,
                         edit_nurse, edit_patient, new_nurse, nurse_details,
                         nurses, patient_details, patients, user_login,
                         user_logout)

urlpatterns = [
    # Authentication URLS
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),


    ## Nurses URLs
    path("nurses/", nurses, name="nurses"),
    path("new-nurse/", new_nurse, name="new-nurse"),
    path("admin-edit-nurse/", admin_edit_nurse, name="admin-edit-nurse"),
    path("edit-nurse/", edit_nurse, name="edit-nurse"),
    path("delete-nurse/", delete_nurse, name="delete-nurse"),
    path("nurses/<int:nurse_id>/", nurse_details, name="nurse-details"),
    

    ## Patients URLs
    path("patients/", patients, name="patients"),
    path("new-patient/", create_patient, name="new-patient"),
    path("patients/<int:patient_id>/",  patient_details, name="patient-details"),
    path("edit-patient/", edit_patient, name="edit-patient"),
]