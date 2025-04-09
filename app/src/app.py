from flask import Flask, abort, flash, redirect, request, render_template, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from flask_mysqldb import MySQL
from Config import config 
from models.ModelUsers import ModelUsers
from models.entities.users import User

app = Flask(__name__)
db = MySQL(app)
login_manager_app = LoginManager(app)

####### Solo poner las rutas que llevan a las paginas principales aqui #######


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/inicio")
def inicio():
    return render_template("public/index.html")


@app.route("/camiseta")
def camiseta():
    return render_template("public/Camiseta.html")


@app.route("/favoritos")
def favoritos():
    return render_template("public/Favoritos.html")


@app.route("/formulario")
def formulario():
    return render_template("public/Formulario.html")


@app.route("/historial")
@login_required
def historial():
    return render_template("public/Historial.html")


@app.route("/perfil")
@login_required
def perfil():
    return render_template("public/perfil.html")


@app.route("/recetas")
def recetas():
    return render_template("public/Recetas.html")


@app.route("/resultados")
def resultados():
    return render_template("public/Resultados.html")


@app.route("/subir")
def subir():
    return render_template("public/Subir.html")


@app.route("/tienda")
def tienda():
    return render_template("public/tienda.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(0, request.form['username'], request.form['password'], 0)
        logged_user = ModelUsers.login(db, user)
        if logged_user != None:
            login_user(logged_user)

            if logged_user.usertype == 1:
                #Pendiente: Modificar el html de admin para que se vea decente, agregar panel de control#
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("inicio"))
        else:
            flash("Acceso rechazado...", "danger")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

##############################################################################

##               El resto del desmadre ponerlo aqui                         ## 

## Funcion para validar que el usuario sea admin, se utiliza en las rutas que necesiten acceso de admin ##
def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        # Verificar si el usuario está autenticado y es un administrador
        if not current_user.is_authenticated or current_user.usertype != 1:
            abort(403)  # Acceso prohibido
        return func(*args, **kwargs)
    return decorated_view


@login_manager_app.user_loader
def load_user(id):
    return ModelUsers.get_by_id(db, id)

#Cualquier ruta que requiera permisos de administrador debe de ir debajo de esta linea# 

@app.route("/admin")
@admin_required
@login_required
def admin():
    return render_template("admin/admin.html")

##############################################################################


# No poner nada debajo de main#
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run(debug=True)
