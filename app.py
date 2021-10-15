#from types import _T1
from typing import Dict
from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request


app = Flask(__name__, template_folder='template')

lista_usuarios = ["Andrés", "Sandra", "Danna", "Juan", "Rosangela", "Yamith"]
listas_peliculas = {
    1:{'titulo':"Película ",'cuerpo':"Sipnosis", 'imagen':'img'},
    2:{'titulo':"Película ", 'cuerpo': "Sinopsis", 'imagen':'img'},
    3:{'titulo':"Película ", 'cuerpo': "Sinopsis", 'imagen':'img'},
}
iniciar_sesion = False
cambiar_datos = False
contrasena_ = False
@app.route("/", methods = ["GET"])
def Inicio(): 
    return "<h1>Bienvenido</h1>"

@app.route("/registro", methods =["GET", "POST"])
def Registro(): 
    if request.method == "GET":
        return render("registro.html", contrasena_ = True)
    else: 
        iniciar_sesion = True
        return redirect("/perfil")

@app.route("/Ingreso", methods = ["GET", "POST"])
def Ingreso():
    return "<h1>Inicio de sesión</h1>"

@app.route("/perfil", methods = ["GET", "POST"])
def Perfil():
    if request.method == "GET":
        return render("perfil.html")
    else:
        cambiar_datos= True
        return redirect ("/") 

@app.route("/mis_peliculas" , methods = ["GET", "POST"])

def Mis_peliculas():
    
    #if request.method == "GET": 
    return render("mis_peliculas.html", listas_peliculas = listas_peliculas) 

    #else:
        #return redirect ("/mis_peliculas")

#@app.route("/cerrar_sesion", methods = ["GET", "POST"])

#def cerrar_sesion():
    #return render("") 





    

    #lista_peliculas=lista_peliculas
if __name__=="__main__":
    app.run(debug=True)