from flask import render_template, redirect, request
from usuario_cr_app import app
from usuario_cr_app.models.usuario import Users

@app.route('/')
def inicio():
    print ("Entre a inicio")
    return render_template('crear.html')

@app.route('/create_users', methods=["POST"])
def create_users():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Users.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/crear')


@app.route("/crear")
def crear():
    # llamar al método de clase get all para obtener todos los usuarios
    all_users = Users.get_all()
    print(all_users)
    return render_template("leer.html", all_users=all_users )

