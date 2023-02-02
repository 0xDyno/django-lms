from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import reverse

from . import utils
from .forms import CreateGroupForm, UpdateGroupForm
from .models import GroupModel


def all_groups_view(request):
    groups = GroupModel.objects.all().order_by("-start_date")
    context = {"all_groups": groups}
    return render(request, "groups/list.html", context=context)


def group_view(request, pk: int):
    group = get_object_or_404(GroupModel, pk=pk)
    
    is_started = utils.is_started(group.start_date)
    
    context = {"group": group, "started": is_started}
    return render(request, "groups/group.html", context=context)


def create_group_view(request):
    if request.method == "GET":
        form = CreateGroupForm()
    
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        
        if form.is_valid():
            group = form.save()
            return HttpResponseRedirect("/groups/" + str(group.pk))
    
    context = {"form": form}
    return render(request, "groups/create.html", context=context)


def edit_group_view(request, pk: int):
    group = get_object_or_404(GroupModel, pk=pk)
    
    if request.method == "GET":
        form = UpdateGroupForm(instance=group)
    elif request.method == "POST":
        form = UpdateGroupForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse("group:info", kwargs={"pk": pk}))
    
    context = {"form": form, "group": group}
    return render(request, "groups/edit.html", context=context)


def delete_group_view(request, pk: int):
    group = get_object_or_404(GroupModel, pk=pk)
    
    if request.method == "POST":
        group.delete()
        return HttpResponseRedirect(reverse("group:all"))
    
    return render(request, "groups/delete.html", context={"group": group})
