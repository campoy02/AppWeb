# Para Manejo de Archivos (Ver ruta de "/Subir")
import os
# Numeros aleatorios (Ver la ruta de "/subir")
from random import randint
# Para "Sanitizar" los nombres de archivo, evitar caracteres problematicos (Ver la ruta de "/subir")
from werkzeug.utils import secure_filename
# Para reducir la resolucion de la imagen (Ver la ruta "/subir")
# Efectivamente, tuve que importar como 4 cosas para una sola ruta xd
from PIL import Image
# Cosas del flask
from flask import Flask, abort, flash, redirect, request, render_template, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# Para los decoradores (Ver funcion de Admin Requiered)
from functools import wraps
# Modulos propios
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


####### Solo poner las rutas que llevan a las paginas principales aqui #######


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/inicio")
def inicio():
    return render_template("public/index.html")

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
    return render_template("public/perfil.html", usuario=current_user)


@app.route("/recetas")
def recetas():
    return render_template("public/Recetas.html")
################################################
# Ruta para cargar una receta con una ID especifica


@app.route("/recetas/<int:id>")
def recetasid(id):
    PaginaRec = ModelPagina.RecetaPorID(db, id)
    return render_template("public/RecetasID.html", receta=PaginaRec)


@app.route("/votar", methods=["POST"])
def votar():
    estrellas = request.form.get("rating")
    id = request.form.get("IDReceta")
    ModelPagina.ActualizarVotos(db, estrellas, id)

    return redirect(url_for("recetasid", id=id))

# Buscador


@app.route("/resultados", methods=["GET"])
def resultados():
    query = request.args.get("q", "").strip()
    resultados = ModelPagina.buscar_recetas(db, query)
    return render_template("public/Resultados.html", resultados=resultados, busqueda=query)


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

            if not os.path.exists(app.config['UPLOAD_PATH']):
                os.makedirs(app.config['UPLOAD_PATH'])
            # Favor de actualizar los comentarios en caso de cambiar alguno de estos limites
            TMAX = 5 * 1024 * 1024  # Tamaño maximo actual: 5MB por imagen
            RMAX = (1500, 1200)  # Resolucion maxima actual:  1000x1200

            if img.content_length > TMAX or img2.content_length > TMAX:
                flash(
                    "Una de las imagenes excede los 5MB, Favor de ingresar un archivo mas ligero")
                return redirect(url_for('subir'))

            # Nomeclatura de el nombre = Numero aleatorio entre 1 a 1000 + ID de el usuario que la subio
            numero = randint(1, 1000)
            id = current_user.id

            nombrearchivo = (str(numero) + str(id))
            custom_filename = nombrearchivo
            file_extension = os.path.splitext(img.filename)[1]
            new_filename = f"{custom_filename}{file_extension}"

            nombrearchivo2 = (nombrearchivo + "apoyo")
            extension2 = os.path.splitext(img2.filename)[1]
            nombreimg2 = f"{nombrearchivo2}{extension2}"

            img_pil = Image.open(img)
            img_pil2 = Image.open(img2)

            img_pil.thumbnail(RMAX)
            img_pil2.thumbnail(RMAX)

            # Ruta desde root para guardar las imagenes en uploads
            file_path = os.path.join(
                app.config['UPLOAD_PATH'], secure_filename(new_filename))
            img_pil.save(file_path)

            file_path2 = os.path.join(
                app.config["UPLOAD_PATH"], secure_filename(nombreimg2))
            img_pil2.save(file_path2)

            # Ruta para que los HTML la puedan referencias
            ruta1 = f"../../static/uploads/" + new_filename
            ruta2 = f"../../static/uploads/" + nombreimg2

            Pagina = pagina(0, nombre, autor, cantidadpersonas, tiempo, dificultad,
                            ingredientes, tips, preparacion, ruta1, ruta2, current_user.id, 0, 0)
            print(Pagina)
            ModelPagina.agregar(db, Pagina)

        flash("Recipe uploaded successfully!", "success")
        return redirect(url_for('subir'))

    return render_template("public/Subir.html")

# Ruta para la pagina de cambiar nombres


@app.route("/perfil/cambiarnombre", methods=["GET", "POST"])
def cambiarnombre():

    if request.method == "POST":
        nuevonombre = request.form["NuevoNom"]
        ModelUsers.actualizarnombre(db, nuevonombre, current_user.id)

        return redirect(url_for("cambiarnombre"))
    else:
        return render_template("public/CambiarNombre.html", usuario=current_user)


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
    receta = ModelPagina.RecetaPorID(db, id)
    if receta:

        Ruta1 = receta.rutaimg
        Ruta2 = receta.rutaimgapoyo

        RutaFull1 = os.path.join(
            app.config['UPLOAD_PATH'], os.path.basename(Ruta1))
        RutaFull2 = os.path.join(
            app.config['UPLOAD_PATH'], os.path.basename(Ruta2))

        ModelPagina.eliminar(db, id)
        flash("Receta eliminada exitosamente", "success")

        try:
            if os.path.exists(RutaFull1):
                os.remove(RutaFull1)
            if os.path.exists(RutaFull2):
                os.remove(RutaFull2)

        except Exception as e:
            flash(f"Error al eliminar las imágenes: {str(e)}", "danger")
    return redirect(url_for("admin"))


##############################################################################
# No poner nada debajo de main#
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run(debug=True)
