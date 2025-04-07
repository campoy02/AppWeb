from flask import Flask, request, render_template

app = Flask(__name__)

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
def historial():
    return render_template("public/Historial.html")

@app.route("/perfil")
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




if __name__ == "__main__":
    app.run(debug=True)