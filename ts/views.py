from django.shortcuts import render
from .models import Student
from .forms import submitdata
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def index(request):
    students = Student.objects.all()
    print(students)
    return render(request, 'index.html', {'st': students})


def submitstudent(request):
    print(f"request: {request}")
    if request.method == 'POST':
        form = submitdata(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "submitted")
            return redirect('home')
    else:
        form = submitdata()
        return render(request, 'submitdata.html', {'form': form})
