from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from appointments.models import Appointment, NurseSchedule, VaccineSchedule
from recordsapp.models import Vaccine
from users.models import Patient


# Create your views here.
@login_required(login_url="/users/login/")
def vaccine_schedules(request):
    schedules = VaccineSchedule.objects.all()
    vaccines = Vaccine.objects.all()
    context = {
        "schedules": schedules,
        "vaccines": vaccines
    }
    return render(request, "appointments/vaccine_schedules.html", context)


@login_required(login_url="/users/login/")
def new_session(request):
    if request.method == "POST":
        vacine_id = request.POST.get("vaccine_id")
        session_date = request.POST.get("session_date")

        session = VaccineSchedule.objects.create(
            vaccine_id=vacine_id,
            session_date=session_date
        )
        return redirect("schedules")

    return render(request, "appointments/new_session.html")

@login_required(login_url="/users/login/")
def book_appointment(request):
    if request.method == "POST":
        session_id = request.POST.get("session_id")
        patient_id = request.POST.get("patient_id")
        
        vaccine_schedule = VaccineSchedule.objects.get(id=session_id)

        patient = Patient.objects.get(user_id=patient_id)

        Appointment.objects.create(
            session=vaccine_schedule,
            patient=patient
        )

        vaccine_schedule.available_slots -= 1
        vaccine_schedule.occupied_slots += 1
        vaccine_schedule.save()

        return redirect(f"/users/patients/{patient.id}/")
        

    return render(request, "appointments/book_appointment.html")


@login_required(login_url="/users/login/")
def assign_nurse_schedule(request):
    if request.method == "POST":
        nurse_id = request.POST.get("nurse_id")
        schedule_id = request.POST.get("schedule_id")

        NurseSchedule.objects.create(
            nurse_id=nurse_id,
            vaccine_schedule_id=schedule_id
        )
        return redirect("nurses")
    
    return render(request, "appointments/schedule_nurse.html")


@login_required(login_url="/users/login/")
def cancel_nurse_schedule(request, schedule_id=None):
    schedule = NurseSchedule.objects.get(id=schedule_id)
    schedule.status = "Declined"
    schedule.save()
    return redirect(f"/users/nurses/{schedule.nurse.id}/")

@login_required(login_url="/users/login/")
def cancel_patient_appointment(request, appointment_id=None):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.accepted = "Cancelled"
    appointment.save()
    return redirect(f"/users/patients/{appointment.patient.id}/")