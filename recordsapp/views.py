from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from appointments.models import VaccineSchedule
from recordsapp.models import VaccinationRecord, Vaccine, VaccineDelivery
from users.models import Nurse, Patient


# Create your views here.
@login_required(login_url="/users/login/")
def vaccines(request):
    vaccines = Vaccine.objects.all()

    paginator = Paginator(vaccines, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "vaccines": vaccines,
        "page_obj": page_obj
    }
    return render(request, "vaccines/vaccines.html", context)

@login_required(login_url="/users/login/")
def new_vaccine(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company = request.POST.get("company")
        dosage = request.POST.get("dosage")
        description = request.POST.get("description")
        quantity = request.POST.get("quantity")

        Vaccine.objects.create(
            name=name,
            company=company,
            dosage_per_immunization=dosage,
            description=description,
            quantity=quantity
        )

        return redirect("vaccines")

    return render(request, "vaccines/new_vaccine.html")

@login_required(login_url="/users/login/")
def edit_vaccine(request):
    if request.method == "POST":
        vaccine_id = request.POST.get("vaccine_id")
        name = request.POST.get("name")
        company = request.POST.get("company")
        dosage = request.POST.get("dosage")
        description = request.POST.get("description")
        
        vaccine = Vaccine.objects.get(id=vaccine_id)
        vaccine.name=name
        vaccine.company=company
        vaccine. dosage_per_immunization=dosage
        vaccine.description=description
        vaccine.save()
        

        return redirect("vaccines")

    return render(request, "vaccines/edit_vaccine.html")


@login_required(login_url="/users/login/")
def new_vaccine_delivery(request):
    if request.method == "POST":
        vaccine_id = request.POST.get("vaccine_id")
        amount = float(request.POST.get("amount"))

        user_input = {
            "vaccine_id": vaccine_id,
            "amount": amount
        }

        print(user_input)
        
        
        vaccine = Vaccine.objects.get(id=vaccine_id)

        VaccineDelivery.objects.create(
            vaccine=vaccine,
            amount_delivered=amount
        )

        vaccine.quantity += amount
        vaccine.save()
    
        return redirect("vaccines")


    return render(request, "vaccines/new_vaccine_delivery.html")


@login_required(login_url="/users/login/")
def vaccinations(request):
    vaccinations = VaccinationRecord.objects.all()
    patients = Patient.objects.all()
    vaccines = Vaccine.objects.all()
    vaccine_schedules = VaccineSchedule.objects.all()
    context = {
        "vaccinations": vaccinations,
        "patients": patients,
        "vaccines": vaccines,
        "vaccine_schedules": vaccine_schedules
    }
    return render(request, "vaccinations/vaccinations.html", context)


@login_required(login_url="/users/login/")
def vaccinate_patient(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        nurse_id = request.POST.get("nurse_id")
        vaccine_id = request.POST.get("vaccine_id")
        vaccine_schedule_id = request.POST.get("vaccine_schedule_id")

        patient = Patient.objects.get(id=patient_id)
        vaccine = Vaccine.objects.get(id=vaccine_id)

        vaccine_schedule = VaccineSchedule.objects.get(id=vaccine_schedule_id)

        description = f"Patient {patient.user.name} Vaccinated with 1 dose of {vaccine.name} at slot {str(vaccine_schedule)}"
        
        nurse = Nurse.objects.get(user_id=nurse_id)

        VaccinationRecord.objects.create(
            patient_id=patient_id,
            vaccine_id=vaccine_id,
            nurse=nurse,
            vaccine_schedule_id=vaccine_schedule_id,
            description=description
        )

        return redirect("vaccinations")
    return render(request, "vaccinations/vaccinate.html")
