from django.shortcuts import render, redirect
from . import MovieApi
import json
# Create your views here.
def HomePage(request):
    Web = request.session.get("Web")
    Web = (" ")
    request.session["Web"] = Web

    Movie = request.session.get("Movie")
    Movie =  {'nothing':'nothing'}
    request.session["Movie"] = Movie
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge

    counter = request.session.get("counter")
    bridge = request.session.get("bridge")
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    counter = 0 
    request.session['counter'] = counter
    ship = request.session.get("ship")
    ship = ["nothing"] * 3
    request.session["ship"] = bridge

    return render(request, 'HomePage.html')
def PickActors(request):
    counter = request.session.get("counter")
    bridge = request.session.get("bridge")
    counter = counter + 1
    request.session['counter'] = counter
    bridge[0] = MovieApi.ActorChoice()
    bridge[1] = MovieApi.ActorChoice()
    bridge[2] = MovieApi.ActorChoice()
    request.session["bridge"] = bridge
    return render(request, 'pickActors.html')

def PickGenre(request):
    choiceArry = MovieApi.getGenresId()
    counter = request.session.get("counter")
    bridge = request.session.get("bridge")
    counter = counter + 1
    bridge[0] = choiceArry[0]
    bridge[1] = choiceArry[1]
    bridge[2] = choiceArry[2]
    request.session['counter'] = counter
    request.session["bridge"] = bridge
    return render(request, 'pickGenre.html')

def PickContentRating(request):
    return render(request, 'PickContentRating.html')

def babies(request):
    Movie = MovieApi.MovieByRating("G")
    request.session["Movie"] = Movie
    return render(request, "LoadRating.html")

def kids(request):
    Movie = MovieApi.MovieByRating("PG")
    request.session["Movie"] = Movie
    return render(request,"LoadRating.html")
def adults(request):
    Movie = MovieApi.MovieByRating("R")
    request.session["Movie"] = Movie
    return render(request,"LoadRating.html")

def teens(request):
    Movie = MovieApi.MovieByRating("PG-13")
    request.session["Movie"] = Movie
    return render(request,"LoadRating.html")

def LoadActors0(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/done")
    ship[counter - 1] = bridge[0]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadActors.html')

def LoadGenres0(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/Done")
    ship[counter - 1] = bridge[0]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadGenre.html')



def LoadActors1(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/done")
    ship[counter - 1] = bridge[1]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadActors.html')

def LoadGenres1(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/Done")
    ship[counter - 1] = bridge[1]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadGenre.html')

def LoadActors2(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/done")
    ship[counter - 1] = bridge[2]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadActors.html')


def LoadGenres2(request):
    bridge = request.session.get("bridge")
    ship = request.session.get("ship")
    counter = request.session.get("counter")
    if counter > 3:
        return redirect("/Done")
    ship[counter - 1] = bridge[2]
    bridge = ["nothing"] * 3
    request.session["bridge"] = bridge
    request.session["ship"] = ship 
    return render(request, 'LoadGenre.html')



def done(request):
    ship = request.session.get("ship")
    Movie = request.session.get("Movie")
    Movie = MovieApi.actorCrossRefrence(ship[0]["name"], ship[1]["name"],ship[2]["name"])
    request.session["Movie"] = Movie
    OmbdInfo = MovieApi.titleSearchOmbd(Movie["title"])
    Pic = request.session.get("Pic")
    Pic = OmbdInfo.get("Poster", "None")
    if Pic == "None":
        Pic ="https://i.imgur.com/85WKJwD.png"
    request.session["Pic"] = Pic

    return render(request, 'done.html')
    

def Done(request):
    ship = request.session.get("ship")
    Movie = request.session.get("Movie")
    Movie = MovieApi.randomizeGenre(ship)
    request.session["Movie"] = Movie
    OmbdInfo = MovieApi.titleSearchOmbd(Movie["title"])
    Pic = request.session.get("Pic")
    Pic = OmbdInfo.get("Poster", "None")
    if Pic == "None":
        Pic ="https://i.imgur.com/85WKJwD.png"
    request.session["Pic"] = Pic
    Web  = request.session.get("Web")
    Web = OmbdInfo.get("Website", "Sorry no Website")
    request.session["Web"] = Web

    return render(request,'done.html')

def Alldone(request):
    Movie = {"nothing ": "nothing"}
    Movie = request.session.get("Movie")
    OmbdInfo = MovieApi.titleSearchOmbd(Movie['title'])
    Pic = request.session.get("Pic")
    Pic = OmbdInfo.get("Poster", "None")
    if Pic == "None":
        Pic ="https://i.imgur.com/85WKJwD.png"
    request.session["Pic"] = Pic
    Web  = request.session.get("Web")
    Web = OmbdInfo.get("Website", "No Website, sorry")
    return render(request,'done.html')
