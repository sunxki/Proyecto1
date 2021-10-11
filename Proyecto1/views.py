from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Champ:

    def __init__(self,name, rol):
        self.name = name
        self.rol = rol

def saludo(request):
    Vayne = Champ("Vayne" , "ADC")

    return render(request,"home.html",{
        "characterName": Vayne.name,
        "characterRol": Vayne.rol
    })

def calculadora(request,a,b):
    division = a/b
    _time = datetime.datetime.now()

    return render(request,"calculator.html", {
        "First_value": a,
        "Second_value": b,
        "division": round(division,4),
        "time":_time.now()
    })





