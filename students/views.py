from django.middleware.csrf import get_token
from django.shortcuts import HttpResponse, HttpResponseRedirect

from . import utils
from .forms import StudentForm
from .models import StudentModel


def home_view(request):
    page = """<center>
                <h1> Home </h1>
                <a href="/students/"> All students </a>
           </center>"""
    return HttpResponse(page)


def all_students_view(request):
    students = StudentModel.objects.all()
    
    page = f"""<center>
           <h1>All students</h1>
           <a href="/"> Home page </a> |
           <a href="create"> Create </a> <br><br>
           {utils.get_table_with_students(students)}
           </center>"""
    
    return HttpResponse(page)


def student_view(request, pk: int):
    if StudentModel.objects.last().pk < pk:
        return HttpResponse(utils.not_found())
    
    st = StudentModel.objects.get(pk=pk)
    
    if request.method == "GET":
        form = StudentForm(instance=st)
        
    if request.method == "POST":
        form = StudentForm(instance=st, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to="/students/")

    page = f"""
            <center>
                <h1> {st.name} {st.surname} </h1>
                <form method="POST">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">
                    <table>
                        {form.as_table()}
                    </table>
                    <br>
                    <input type="submit" value="Save">
                    <a href="delete/{pk}"><input type="button" value="Delete"></a>
                    <a href="/students/"><input type="button" value="Back"></a>
                </form>
            </center>
            """
    return HttpResponse(page)


def create_student_view(request):
    if request.method == "GET":
        form = StudentForm()
        
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/students/")
    
    page = f"""
    <center>
        <form method="POST">
            <table>
                {form.as_table()}
            </table>
            <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">
            <input type="submit" value="Save"> <br> <br>
            <a href="/students/"><input type="button" value="All Students"></a>
        </form>
    </center>
    """
    
    return HttpResponse(page)


def delete_student_view(request, pk: int):
    if StudentModel.objects.last().pk < pk:
        return HttpResponse(utils.not_found())
    
    if request.method == "GET":
        page = f"""<center>Do you want to delete? <br> <br>
                    <form method="POST">
                        <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">
                        <input type="submit" value="Delete">
                        <a href="/students/{pk}">
                            <input type="submit" value="Back">
                        </a>
                    </form>
                </center>
                """
        return HttpResponse(page)
    elif request.method == "POST":
        st = StudentModel.objects.get(pk=pk)
        st.delete()
        return HttpResponseRedirect(redirect_to="/students/")
