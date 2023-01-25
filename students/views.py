from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateStudentForm, UpdateStudentForm
from .models import StudentModel


def home_view(request):
    return render(request, "base/home.html", context={"message": "Home page"})


def all_students_view(request):
    context = {"all_students": StudentModel.objects.all()}
    return render(request, "students/students.html", context=context)


def student_view(request, pk: int):
    if StudentModel.objects.last().pk < pk:
        return render(request, "base/home.html", context={"message": "404. Not Found"})
    
    context = {"st": StudentModel.objects.get(pk=pk)}
    return render(request, "students/student.html", context=context)


def create_student_view(request):
    if request.method == "GET":
        form = CreateStudentForm()
    
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        
        if form.is_valid():
            student = form.save()
            return HttpResponseRedirect("/students/" + str(student.pk))
    
    context = {"form": form}
    return render(request, "students/create.html", context=context)


def edit_student_view(request, pk: int):
    if StudentModel.objects.last().pk < pk:
        return render(request, "base/home.html", context={"message": "404. Not Found"})
    
    student = StudentModel.objects.get(pk=pk)
    
    if request.method == "GET":
        form = UpdateStudentForm(instance=student)
    elif request.method == "POST":
        form = UpdateStudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/students/" + str(pk))
    
    context = {"form": form, "pk": pk}
    return render(request, "students/edit.html", context=context)


def delete_student_view(request, pk: int):
    if StudentModel.objects.last().pk < pk:
        return render(request, "base/home.html", context={"message": "404. Not Found"})
    
    if request.method == "POST":
        student = StudentModel.objects.get(pk=pk)
        student.delete()
        return HttpResponseRedirect("/students/")
    
    return render(request, "students/delete.html", context={"pk": pk})
