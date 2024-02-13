from django.urls import path

from appointments.views import (assign_nurse_schedule, book_appointment,
                                cancel_nurse_schedule,
                                cancel_patient_appointment, new_session,
                                vaccine_schedules)

urlpatterns = [
    path("schedules/", vaccine_schedules, name="schedules"),
    path("book-appointment/", book_appointment, name="book-appointment"),
    path("new-session/", new_session, name="new-session"),
    path("schedule-nurse/", assign_nurse_schedule, name="schedule-nurse"),
    path("cancel-nurse-schedule/<int:schedule_id>/", cancel_nurse_schedule, name="cancel-nurse-schedule"),
    path("cancel-appointment/<int:appointment_id>/", cancel_patient_appointment, name="cancel-appointment"),
]