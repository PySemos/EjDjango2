from django.shortcuts import render
from django.http import HttpResponse
from player.models import Player
def introducir_usuario(request):
    return render(request,"form.html",{})
def get(request):
    try:
        p1=Player(user_name=request.GET["user"],email=request.GET["email"])
        p1.save()
        mensaje="<html>Jugador {} introducido </html>".format(request.GET["user"])
    except:
        mensaje="Ha ocurrido un error"
    return HttpResponse(mensaje)
