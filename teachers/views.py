from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import CreateTeacherForm, UpdateTeacherForm
from .models import TeacherModel


def all_teachers_view(request):
    context = {"all_teachers": TeacherModel.objects.all().order_by("-salary")}
    return render(request, "teachers/teachers.html", context=context)


def teacher_view(request, pk: int):
    teacher = get_object_or_404(TeacherModel, pk=pk)
    
    context = {"teacher": teacher}
    return render(request, "teachers/teacher.html", context=context)


def create_teacher_view(request):
    if request.method == "GET":
        form = CreateTeacherForm()
    
    if request.method == "POST":
        form = CreateTeacherForm(request.POST)
        
        if form.is_valid():
            teacher = form.save()
            return HttpResponseRedirect("/teachers/" + str(teacher.pk))
    
    context = {"form": form}
    return render(request, "teachers/create_teacher.html", context=context)


def edit_teacher_view(request, pk: int):
    teacher = get_object_or_404(TeacherModel, pk=pk)
    
    if request.method == "GET":
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == "POST":
        form = UpdateTeacherForm(instance=teacher, data=request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/teachers/" + str(pk))
    
    context = {"form": form, "pk": pk}
    return render(request, "teachers/edit_teacher.html", context=context)


def delete_teacher_view(request, pk: int):
    if request.method == "POST":
        teacher = get_object_or_404(TeacherModel, pk=pk)
        teacher.delete()
        return HttpResponseRedirect("/teachers/")
    
    return render(request, "teachers/delete_teacher.html", context={"pk": pk})
