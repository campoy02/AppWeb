import os
from random import randint
from flask import Flask, abort, flash, redirect, request, render_template, url_for
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from flask_mysqldb import MySQL
from Config import config
from models.ModelUsers import ModelUsers
from models.entities.users import User
from models.ModelPaginas import ModelPagina
from models.entities.pagina import pagina

app = Flask(__name__)

db = MySQL(app)
login_manager_app = LoginManager(app)
app.config['UPLOAD_PATH'] = 'app/src/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

####### Maneja los archivos aceptados para las imagenes                #######
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

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

## Ruta de Prueba, Sera borrada posteriormente ## 
@app.route("/pruebaimg")
def pruebaimg():
    # Fetch the first recipe from the database
    recetas = ModelPagina.obtenerrecetas(db)
    print(recetas)
    return render_template("public/pruebaimg.html", recetas=recetas)

@app.route("/subir", methods=["GET", "POST"])
@login_required
def subir():
    if request.method == "POST":
        img = request.files['imagen-receta']  
        img2 = request.files['imagenes-apoyo'] 

        nombre = request.form['titulo']
        autor = request.form['autor']
        cantidadpersonas = request.form['personas']
        tiempo = request.form['tiempo']
        dificultad = request.form['dificultad']
        ingredientes = request.form['ingredientes']
        tips = request.form['tips']
        preparacion = request.form['preparacion']

        if img and img.filename and img2 and img2.filename != '':
            # Ensure the upload directory exists
            if not os.path.exists(app.config['UPLOAD_PATH']):
                os.makedirs(app.config['UPLOAD_PATH'])
            
            # Nomeclatura de el nombre = Numero aleatorio entre 1 a 1000 + ID de el usuario que la subio
            numero = randint(1, 1000)
            id = current_user.id

            nombrearchivo = (str(numero) + str(id))
            custom_filename = nombrearchivo  # Change this to your desired filename
            file_extension = os.path.splitext(img.filename)[1]  # Get the original file extension
            new_filename = f"{custom_filename}{file_extension}"  # Combine custom name with the original extension
            
            nombrearchivo2 = (nombrearchivo + "apoyo")
            extension2 = os.path.splitext(img2.filename)[1]
            nombreimg2 = f"{nombrearchivo2}{extension2}"

            # Para guardar las imagenes en el directorio
            file_path = os.path.join(app.config['UPLOAD_PATH'], secure_filename(new_filename))
            img.save(file_path)

            file_path2 = os.path.join(app.config["UPLOAD_PATH"], secure_filename (nombreimg2))
            img2.save(file_path2)

            # Esta otra ruta es para que las pueda leer HTML
            ruta1 = f"../../static/uploads/" + new_filename
            ruta2 = f"../../static/uploads/" + nombreimg2

            Pagina = pagina(0, nombre, autor, cantidadpersonas, tiempo, dificultad, ingredientes, tips, preparacion, ruta1, ruta2, current_user.id, 0)
            print(Pagina)
            ModelPagina.agregar(db, Pagina)
            
        flash("Recipe uploaded successfully!", "success")
        return redirect(url_for('subir'))

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
        # Pa checar si es el formulario de registro
        if "RegNombre" in request.form:
            nombre = request.form["RegNombre"]
            passw = request.form["RegPass"]
            fullname = request.form["RegNCom"]
            mail = request.form["RegMail"]

            user = User(0, nombre, passw, 0, fullname, mail)
            ModelUsers.registrar(db, user)
            flash("Registro exitoso", "success")
            return render_template("auth/login.html")
        # Pa checar si es el formulario de login
        elif "username" in request.form:
            user = User(0, request.form['username'],
                        request.form['password'], 0, 0)
            logged_user = ModelUsers.login(db, user)
            if logged_user is not None:
                login_user(logged_user)

                if logged_user.usertype == 1:
   
                    flash("Bienvenido administrador", "success")
                    return redirect(url_for("admin"))
                else:
                    flash("Inicio de sesion exitoso", "success")
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
        
        if not current_user.is_authenticated or current_user.usertype != 1:
            abort(403)  # Acceso prohibido
        return func(*args, **kwargs)
    return decorated_view


@login_manager_app.user_loader
def load_user(id):
    return ModelUsers.get_by_id(db, id)

# Rutas para administrar recetas
@app.route("/admin")
@admin_required
@login_required
def admin():
    recetas = ModelPagina.obtenerrecetas(db)
    return render_template("admin/recetas.html", recetas=recetas)

@app.route("/admin/eliminar/<int:id>", methods=["POST"])
@admin_required
@login_required
def eliminar_receta(id):
    ModelPagina.eliminar(db, id)
    flash("Receta eliminada exitosamente", "success")
    return redirect(url_for("admin"))




##############################################################################


# No poner nada debajo de main#
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run(debug=True)
