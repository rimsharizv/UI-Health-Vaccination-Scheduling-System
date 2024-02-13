from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import redirect, render

from appointments.models import VaccineSchedule
from users.models import Nurse, Patient, User


# Create your views here.
################ Authentication URLs ##############
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.role == "patient":
                patient = Patient.objects.get(user=user)
                return redirect(f"/users/patients/{patient.id}/")
            elif user.role == "nurse":
                nurse = Nurse.objects.get(user=user)
                return redirect(f"/users/nurses/{nurse.id}/")
                
            return redirect('home') 
    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


############## Patients ####################
@login_required(login_url="/users/login/")
def patients(request):
    patients = Patient.objects.all()

    

    paginator = Paginator(patients, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "patients": patients,
        "page_obj": page_obj
    }
    return render(request, "patients/patients.html", context)

@login_required(login_url="/users/login/")
@transaction.atomic
def create_patient(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        ssn = request.POST.get("ssn")
        address = request.POST.get("address")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        occupation = request.POST.get("occupation")
        race = request.POST.get("race")
        medical_history = request.POST.get("medical_history")

        password = request.POST.get("password")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            role="patient",
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        patient = Patient.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            age=age,
            address=address,
            social_security_number=ssn,
            phone_number=phone_number,
            occupation=occupation,
            medical_history=medical_history,
            race=race
        )

        return redirect("login")

    return render(request, "patients/add_patient.html")

@login_required(login_url="/users/login/")
def patient_details(request, patient_id=None):
    patient = Patient.objects.get(id=patient_id)

    appointments = patient.patientappointments.all()
    appointments_count = patient.patientappointments.all().count()
    vaccinations = patient.patientvaccinations.all()
    vaccinations_count = patient.patientvaccinations.all().count()

    context = {
        "patient": patient,
        "appointments": appointments,
        "appointments_count": appointments_count,
        "vaccinations": vaccinations,
        "vaccinations_count": vaccinations_count,
    }
    return render(request, "patients/patient_details.html", context)


@login_required(login_url="/users/login/")
@transaction.atomic
def edit_patient(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        ssn = request.POST.get("ssn")
        address = request.POST.get("address")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        occupation = request.POST.get("occupation")
        race = request.POST.get("race")
        medical_history = request.POST.get("medical_history")

        patient = Patient.objects.get(id=patient_id)


        patient.user.first_name=first_name
        patient.last_name=last_name
        patient.user.role="patient"
        patient.user.username=username
        patient.user.email=email
        patient.user.save()

       
        patient.first_name=first_name
        patient.last_name=last_name
        patient.gender=gender
        patient.age=age
        patient.address=address
        patient.social_security_number=ssn
        patient.phone_number=phone_number
        patient.occupation=occupation
        patient.medical_history=medical_history
        patient.race=race
        

        return redirect(f"/users/patients/{patient.id}/")

    return render(request, "patients/edit_patient.html")



############### NURSES #######################
@login_required(login_url="/users/login/")
def nurses(request):
    nurses = Nurse.objects.all()
    schedules = VaccineSchedule.objects.all()

    paginator = Paginator(nurses, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "nurses": nurses,
        "page_obj": page_obj,
        "schedules": schedules
    }
    return render(request, "nurses/nurses.html", context)

@login_required(login_url="/users/login/")
def nurse_details(request, nurse_id=None):
    nurse = Nurse.objects.get(id=nurse_id)

    nurse_schedules = nurse.nurseschedules.all()
    appointments_count = nurse.nurseschedules.all().count()

    vaccinations = nurse.nursevaccinations.all()
    vaccinations_count = nurse.nursevaccinations.all().count()

    context = {
        "nurse": nurse,
        "nurse_schedules": nurse_schedules,
        "appointments_count": appointments_count,
        "vaccinations": vaccinations
    }

    return render(request, "nurses/nurse_details.html", context)

@login_required(login_url="/users/login/")
@transaction.atomic
def new_nurse(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        employeeId = request.POST.get("employee_id")
        address = request.POST.get("address")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            role="nurse",
            username=username,
            email=email
        )
        user.set_password("1234")
        user.save()

        nurse = Nurse.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            age=age,
            address=address,
            employeeId=employeeId,
            phone_number=phone_number,
        )
        return redirect("nurses")
    
    return render(request, "nurses/new_nurse.html")

@login_required(login_url="/users/login/")
def admin_edit_nurse(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        employeeId = request.POST.get("employee_id")
        username = request.POST.get("username")
        email = request.POST.get("email")
        nurse_id = request.POST.get("nurse_id")
        nurse = Nurse.objects.get(id=nurse_id)

        # User
        nurse.user.first_name=first_name
        nurse.user.last_name=last_name
        nurse.user.role="nurse"
        nurse.user. username=username
        nurse.user.email=email
        nurse.user.save()

        # Nurse
        nurse.first_name=first_name
        nurse.last_name=last_name
        nurse.gender=gender
        nurse.age=age
        nurse.employeeId=employeeId
        nurse.save()
        
        return redirect("nurses")
    
    return render(request, "nurses/admin_edit_nurse.html")

@login_required(login_url="/users/login/")
def edit_nurse(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        nurse_id = request.POST.get("nurse_id")
        nurse = Nurse.objects.get(id=nurse_id)
        # Nurse
        
        nurse.phone_number = phone_number
        nurse.address = address
        nurse.save()
        
        return redirect("nurses")
    
    return render(request, "nurses/edit_nurse.html")

@login_required(login_url="/users/login/")
def delete_nurse(request):
    if request.method == "POST":
        nurse_id = request.POST.get("nurse_id")

        nurse = Nurse.objects.get(id=nurse_id)
        nurse.delete()
        return redirect("nurses")

    return render(request, "nurses/delete_nurse.html")

