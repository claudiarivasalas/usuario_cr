from usuario_cr_app import app
from usuario_cr_app.controllers import usuarios
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)

