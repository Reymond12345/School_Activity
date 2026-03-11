from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from . models import Student


def index(request):
    return render(request, 'HS/index.html')

def about(request):
    return render(request, 'HS/about.html')

def home(request):
    return render(request, 'HS/home.html')
# Create your views here.
@csrf_protect
def enroll(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()
        
        student = Student.objects.create(
            firstname = firstname,
            lastname = lastname,
            age = int(age) if age else 0,
            gender = gender
        )
        
        info = {
            "submitted":True,
            "firstname":firstname,
            "lastname":lastname,
            "age":age,
            "gender":gender,
        }
        return render(request, "HS/enroll.html", info)
    return render(request, "HS/enroll.html")
