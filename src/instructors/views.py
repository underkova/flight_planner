from django.shortcuts import render
from django.http import HttpResponse
from .models import instructors
def index(request):
    instructors_list = instructors.objects.all()
    return HttpResponse("<h4>кек</h4>", {'instructors': instructors_list})
# Create your views here.
#дальше пойдут запросы как в students
#python manage.py migrate

def planning(request):
    return HttpResponse("<h4>Плана нет, погода нелетная!"
                        " спим, в небе только шамилич</h4>")
def instructor_flight_time(request):
    return HttpResponse("<h4>если вы шамилич ваш налет - 100500 часов</h4><h1>Если вас не устраивает ваш налет, вам <a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'>сюда</a> </h1>")