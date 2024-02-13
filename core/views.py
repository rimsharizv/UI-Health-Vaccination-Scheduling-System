from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from recordsapp.models import Vaccine
from users.models import Nurse, Patient


# Create your views here.
@login_required(login_url="/users/login/")
def home(request):
    user = request.user

    if user.role == "patient":
        patient = Patient.objects.get(user=user)
        return redirect(f"/users/patients/{patient.id}/")
    elif user.role == "nurse":
        nurse = Nurse.objects.get(user=user)
        return redirect(f"/users/nurses/{nurse.id}/")

    patients_count = Patient.objects.all().count()
    nurses_count = Nurse.objects.all().count()
    vaccines_count = Vaccine.objects.all().count()
    context = {
        "patients_count": patients_count,
        "nurses_count": nurses_count,
        "vaccines_count": vaccines_count
    }
    return render(request, "home.html", context)