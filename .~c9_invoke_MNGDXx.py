from flask import Flask,render_template, url_for, request, jsonify,session, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from cs50 import SQL
from tempfile import mkdtemp

from modelo.categoria import *
from modelo.cliente import *
from modelo.feria import *
from modelo.emprendedor import *
from modelo.emprendimiento import *
from modelo.producto import *
from modelo.servicio import *
from clases import *
from helpers import *

db = SQL("sqlite:///wabisabi.db")
app = Flask(__name__)
tipo_user = ""
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
@login_required
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    session.clear()
    if request.method == "POST":
        correo = request.form.get('correo')
        contraseña = request.form.get("contrasena")
        tipo = request.form.get('tipo')
        if(tipo == "cliente"):
            res = iniciarSesionCliente(db, correo, contraseña)
            if(res == -1):
                print("llamando función flash-------------------------------------------------------------")
                flash("Contraseña/Correo incorrecto, intente otra vez.")
                return redirect(url_for("login"))
            else:
                session["user_id"] = res["id_cliente"]
                session["tipo"] = "cliente"
                return render_template("cliente-index.html")

        elif (tipo == "emprendedor"):
            res = inciarSesionEmprendedor(db, correo, contraseña)
            if(res == -1):
                print("llamando función flash-------------------------------------------------------------")
                flash("Contraseña/Correo incorrecto, intente otra vez.")
                return redirect(url_for("login"))
            else:
                session["user_id"] = res["id_emprendedor"]
                session["tipo"] = "emprendedor"
                return render_template("emprendedor-index.html")
        else:
            return "ERROR al escoger el tipo de usuario"
    else:
        return render_template("login.html")

@app.route("/cerrarSesion")
@login_required
def cerrarSesion():
    session.clear()
    return redirect("/")


@app.route("/registrarse")
def registrarse():
    return render_template("registrarse.html")
#######################################emprendedor####################################################

@app.route("/emprendedor/emprendimiento")
@login_required
def emprendedorEmprendimiento():
    return render_template("emprendedor-emprendimiento.html")



# REVISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR
@app.route('/categorias', methods=['GET','POST'])
def categorias():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        url = request.form.get("url_foto")

        objeto_categoria = Categoria(0, nombre, descripcion, url)
        res  = insertarCategoria(db,objeto_categoria)
        lista_categorias = mostrarCategoria(db)
        return render_template("admin-categoria.html", lista_categorias = lista_categorias)
    else:
        return render_template("index.html")


#########################################################################################################
#                                           ADMINISTRACION                                              #
#########################################################################################################

@app.route('/admin')
def admin():
    return render_template("administracion.html")

#-------------------------------------------------------------------------------------------------------#
#---------------------------------------------- Categoría ----------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

@app.route('/admin/categoria', methods = ["GET", "POST"])
def adminCategoria():

    if request.method == "POST":
        ## registrar nueva categoria
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        url = request.form.get("url_foto")

        # esto es con respecto al constructor en clases.py
        objeto_categoria = Categoria(0, nombre, descripcion, url)
        res  = insertarCategoria(db,objeto_categoria)
        lista_categorias = mostrarCategoria(db)
        return render_template("admin-categoria.html", lista_categorias = lista_categorias)
    else:
        lista_categorias = mostrarCategoria(db)
        return render_template("admin-categoria.html", lista_categorias = lista_categorias)

@app.route('/admin/categoria/editarNombre')
def adminCategoriaEditarNombre():
    idCategoria = request.args.get("idCategoria")
    nombre = request.args.get("nombre")
    if (actualizarNombreCategoria(db, idCategoria, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/categoria/editarDescripcion')
def adminCategoriaEditarDescripcion():
    idCategoria = request.args.get("idCategoria")
    descripcion = request.args.get("descripcion")
    if (actualizarDescripcionCategoria(db, idCategoria, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/categoria/editarImagen')
def adminCategoriaEditarImagen():
    idCategoria = request.args.get("idCategoria")
    imagen = request.args.get("imagen")
    if (actualizarUrlFotoCategoria(db, idCategoria, imagen)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#---------------------------------------------- Cliente ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#


@app.route('/admin/cliente', methods = ["GET", "POST"])
def adminCliente():

    if request.method == "POST":
        # el autor tendrá el valor de user si se registró un cliente, y tendrá el valor de admin,
        # si el administrador lo hizo
        autor = request.form.get("autor")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        cedula = request.form.get("cedula")
        departamento = request.form.get("departamento")
        municipio = request.form.get("municipio")
        direccion = request.form.get("direccion")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")
        fecha_nacimiento = request.form.get("fecha_nacimiento")
        contrasena = generate_password_hash(request.form.get("contrasena"))
        url_foto = request.form.get("url_foto")

        objeto_cliente = Cliente(0, nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto)
        res = insertarCliente(db,objeto_cliente)
        if(autor == "user"):
            session["user_id"] = res
            session["tipo"] = "cliente"
            return redirect("/")
        else:
            lista_cliente = mostrarCliente(db)
            return render_template("admin-cliente.html", lista_cliente = lista_cliente)

    else:
        lista_cliente = mostrarCliente(db)
        return render_template("admin-cliente.html", lista_cliente = lista_cliente)

@app.route('/admin/cliente/editarNombre')
def adminClienteEditarNombre():
    idCliente = request.args.get('idCliente')
    nombre = request.args.get('nuevoValor')
    if(actualizarNombreCliente(db, id_cliente, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarApellido')
def adminClienteEditarApellido():
    idCliente = request.args.get('idCliente')
    apellido = request.args.get('nuevoValor')
    if(actualizarApellidoCliente(db, id_cliente, apellido)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarCedula')
def adminClienteEditarCedula():
    idCliente = request.args.get('idCliente')
    cedula = request.args.get('nuevoValor')
    if(actualizarCedulaCliente(db, id_cliente, cedula)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarDpto')
def adminClienteEditarDpto():
    idCliente = request.args.get('idCliente')
    departamento = request.args.get('nuevoValor')
    if(actualizarDepartamentoCliente(db, id_cliente, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarMunicipio')
def adminClienteEditarMunicipio():
    idCliente = request.args.get('idCliente')
    municipio = request.args.get('nuevoValor')
    if(actualizarMunicipioCliente(db, id_cliente, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarDireccion')
def adminClienteEditarDireccion():
    idCliente = request.args.get('idCliente')
    direccion = request.args.get('nuevoValor')
    if(actualizarDireccionCliente(db, id_cliente, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarTel')
def adminClienteEditarTel():
    idCliente = request.args.get('idCliente')
    telefono = request.args.get('nuevoValor')
    if(actualizarTelefonoCliente(db, id_cliente, telefono)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarCorreo')
def adminClienteEditarCorreo():
    idCliente = request.args.get('idCliente')
    correo = request.args.get('nuevoValor')
    if(actualizarCorreoCliente(db, id_cliente, correo)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarNac')
def adminClienteEditarNac():
    idCliente = request.args.get('idCliente')
    fechaNac = request.args.get('nuevoValor')
    if(actualizarFechaNacCliente(db, id_cliente, fechaNac)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarContra')
def adminClienteEditar():
    idCliente = request.args.get('idCliente')
    contra = request.args.get('nuevoValor')
    if(actualizarContrasenaCliente(db, id_cliente, contra)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarImagen')
def adminClienteEditarImagen():
    idCliente = request.args.get('idCliente')
    imagen = request.args.get('nuevoValor')
    if(actualizarUrl_FotoCliente(db, id_cliente, imagen)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#--------------------------------------- Emprendedor ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

@app.route('/admin/emprendedor', methods = ["GET", "POST"])
def adminEmprendedor():

    if request.method == "POST":
        autor = request.form.get("autor")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        cedula = request.form.get("cedula")
        departamento = request.form.get("departamento")
        municipio = request.form.get("municipio")
        direccion = request.form.get("direccion")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")
        fecha_nacimiento = request.form.get("fecha_nacimiento")
        contrasena = request.form.get("contrasena")
        url_foto = request.form.get("url_foto")
        objeto_emprendedor = Emprendedor(0, nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto)
        res = insertaremprendedor(db,objeto_emprendedor)
        if(autor == "user"):
            session["user_id"] = res
            session["tipo"] = "emprendedor"
            return redirect("/")
        else:
            lista_cliente = mostrarCliente(db)
            return render_template("admin-cliente.html", lista_cliente = lista_cliente)
    else:
       lista_emprendedor = mostrarEmprendedor(db)
       return render_template("admin-emprendedor.html", lista_emprendedor = lista_emprendedor)

@app.route('/admin/emprendedor/editarNombre')
def adminEmprendedorEditarNombre():
    idEmprendedor = request.args.get('idEmprendedor')
    nombre = request.args.get('nombre')
    if(actualizarNombreEmprendedor(db, idEmprendedor, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarApellido')
def adminEmprendedorEditarApellido():
    idEmprendedor = request.args.get('idEmprendedor')
    apellido = request.args.get('apellido')
    if(actualizarApellidoEmprendedor(db, idEmprendedor, apellido)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarCedula')
def adminEmprendedorEditarCedula():
    idEmprendedor = request.args.get('idEmprendedor')
    cedula = request.args.get('cedula')
    if(actualizarCedulaEmprendedor(db, idEmprendedor, cedula)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarDepartamento')
def adminEmprendedorEditarDepartamento():
    idEmprendedor = request.args.get('idEmprendedor')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoEmprendedor(db, idEmprendedor, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarMunicipio')
def adminEmprendedorEditarMunicipio():
    idEmprendedor = request.args.get('idEmprendedor')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioEmprendedor(db, idEmprendedor, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarDireccion')
def adminEmprendedorEditarDireccion():
    idEmprendedor = request.args.get('idEmprendedor')
    dereccion = request.args.get('direccion')
    if(actualizarDireccionEmprendedor(db, idEmprendedor, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarTelefono')
def adminEmprendedorEditarTelefono():
    idEmprendedor = request.args.get('idEmprendedor')
    telefono = request.args.get('telefono')
    if(actualizarTelefonoEmprendedor(db, idEmprendedor, telefono)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarCorreo')
def adminEmprendedorEditarCorreo():
    idEmprendedor = request.args.get('idEmprendedor')
    correo = request.args.get('correo')
    if(actualizarCorreoEmprendedor(db, idEmprendedor, correo)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarFechaNacimiento')
def adminEmprendedorEditarFechaNacimiento():
    idEmprendedor = request.args.get('idEmprendedor')
    fecha_nacimiento = request.args.get('fecha_nacimiento')
    if(actualizarFechaNacEmprendedor(db, idEmprendedor, fecha_nacimiento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarContrasena')
def adminEmprendedorEditarContrasena():
    idEmprendedor = request.args.get('idEmprendedor')
    contrasena = request.args.get('nuevoValor')
    if(actualizarContrasenaEmprendedor(db, idEmprendedor, contrasena)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarUrlFoto')
def adminEmprendedorEditarUrlFoto():
    idEmprendedor = request.args.get('idEmprendedor')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoEmprendedor(db, idEmprendedor, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#--------------------------------------- Emprendimiento ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

@app.route('/admin/emprendimiento', methods = ["GET", "POST"])
def adminEmprendimiento():

    if request.method == "POST":

        id_categoria = request.form.get("id_categoria")
        id_emprendedor = request.form.get("id_emprendedor")
        nombre = request.form.get("nombre")
        departamento = request.form.get("departamento")
        municipio = request.form.get("municipio")
        direccion = request.form.get("direccion")
        descripcion = request.form.get("descripcion")
        url_foto = request.form.get("url_foto")
        link_facebook = request.form.get("link_facebook")
        link_youtube = request.form.get("link_youtube")
        link_instagram = request.form.get("link_instagram")
        link_twitter = request.form.get("link_twitter")

        objeto_emprendimiento = Emprendimiento(0, id_categoria, id_emprendedor, nombre, departamento, municipio, direccion, descripcion, url_foto, link_facebook, link_youtube, link_instagram, link_twitter)
        res = insertarEmprendimiento(db, objeto_emprendimiento)
        lista_emprendimiento = mostrarEmprendimiento(db)
        return render_template("admin-emprendimiento.html", lista_emprendimiento = lista_emprendimiento)
    else:
        lista_emprendimiento = mostrarEmprendimiento(db)
        return render_template("admin-emprendimiento.html", lista_emprendimiento = lista_emprendimiento)

@app.route('/admin/emprendimiento/editarNombre')
def adminEmprendimientoEditarNombre():
    idEmprendimiento = request.args.get('idEmprendimiento')
    nombre = request.args.get('nombre')
    if(actualizarNombreEmprendimiento(db, id_emprendimiento, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDepartamento')
def adminEmprendimientoEditarDepartamento():
    idEmprendimiento = request.args.get('idEmprendimiento')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoEmprendimiento(db, id_emprendimiento, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarMunicipio')
def adminEmprendimientoEditarMunicipio():
    idEmprendimiento = request.args.get('idEmprendimiento')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioEmprendimiento(db, id_emprendimiento, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDireccion')
def adminEmprendimientoEditarDireccion():
    idEmprendimiento = request.args.get('idEmprendimiento')
    direccion = request.args.get('direccion')
    if(actualizarDireccionEmprendimiento(db, id_emprendimiento, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDescripcion')
def adminEmprendimientoEditarDescripcion():
    idEmprendimiento = request.args.get('idEmprendimiento')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionEmprendimiento(db, id_emprendimiento, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarUrlFoto')
def adminEmprendimientoEditarUrlFoto():
    idEmprendimiento = request.args.get('idEmprendimiento')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoEmprendimiento(db, id_emprendimiento, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkFacebook')
def adminEmprendimientoEditarLinkFacebook():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_facebook = request.args.get('link_facebook')
    if(actualizarLinkFacebookEmprendimiento(db, id_emprendimiento, link_facebook)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkYoutube')
def adminEmprendimientoEditarLinkYoutube():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_youtube = request.args.get('link_youtube')
    if(actualizarLinkYoutubeEmprendimiento(db, id_emprendimiento, link_youtube)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkInstagram')
def adminEmprendimientoEditarLinkInstagram():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_instagram = request.args.get('link_instagram')
    if(actualizarLinkInstagramEmprendimiento(db, id_emprendimiento, link_instagram)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkTwitter')
def adminEmprendimientoEditarLinkTwitter():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_twitter = request.args.get('link_twitter')
    if(actualizarLinkTwitterEmprendimiento(db, id_emprendimiento, link_twitter)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#------------------------------------------------ Feria ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

@app.route('/admin/feria', methods = ["GET", "POST"])
def adminFeria():

    if request.method == "POST":

        id_emprendimiento = request.form.get("id_emprendimiento")
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        departamento = request.form.get("departamento")
        municipio = request.form.get("municipio")
        direccion = request.form.get("direccion")
        fecha_inicio = request.form.get("fecha_inicio")
        fecha_fin = request.form.get("fecha_fin")
        url_foto = request.form.get("url_foto")

        objeto_feria = Feria(0, id_emprendimiento, nombre, descripcion, departamento, municipio, direccion, fecha_inicio, fecha_fin, url_foto)
        res = insertarFeria(db, objeto_feria)
        lista_feria = mostrarFeria(db)
        return render_template("admin-feria.html", lista_feria = lista_feria)
    else:
        lista_feria = mostrarFeria(db)
        return render_template("admin-feria.html", lista_feria = lista_feria)

@app.route('/admin/feria/editarNombre')
def adminFeriaEditarNombre():
    id_feria = request.args.get('id_feria')
    nombre = request.args.get('nombre')
    if(actualizarNombreFeria(db, id_feria, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDescripcion')
def adminFeriaEditarDescripcion():
    id_feria = request.args.get('id_feria')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionFeria(db, id_feria, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDepartamento')
def adminFeriaEditarDepartamento():
    id_feria = request.args.get('id_feria')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoFeria(db, id_feria, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarMunicipio')
def adminFeriaEditarMunicipio():
    id_feria = request.args.get('id_feria')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioFeria(db, id_feria, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDireccion')
def adminFeriaEditarDireccion():
    id_feria = request.args.get('id_feria')
    direccion = request.args.get('direccion')
    if(actualizarDireccionFeria(db, id_feria, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarFechaInicio')
def adminFeriaEditarFechaInicio():
    id_feria = request.args.get('id_feria')
    fecha_inicio = request.args.get('fecha_inicio')
    if(actualizarFechaInicioFeria(db, id_feria, fecha_inicio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarFechaFin')
def adminFeriaEditarFechaFin():
    id_feria = request.args.get('id_feria')
    fecha_fin = request.args.get('fecha_fin')
    if(actualizarFechaFinFeria(db, id_feria, fecha_fin)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarUrlFoto')
def adminFeriaEditarUrlFoto():
    id_feria = request.args.get('id_feria')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoFeria(db, id_feria, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")


#-------------------------------------------------------------------------------------------------------#
#--------------------------------------------- Producto ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#



@app.route('/admin/producto', methods = ["GET", "POST"])
def adminProducto():

    if request.method == "POST":
        id_emprendimiento = request.form.get("id_emprendimiento")
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        url_foto = request.form.get("url_foto")
        disponible = request.form.get("disponible")

        objeto_producto = Producto(0, id_emprendimiento, nombre, descripcion, precio, url_foto, disponible)
        res = insertarProducto(db, objeto_producto)
        lista_producto = mostrarProducto(db)
        return render_template("admin-producto.html", lista_producto = lista_producto)
    else:
        lista_producto = mostrarProducto(db)
        return render_template("admin-producto.html", lista_producto = lista_producto)

@app.route('/admin/producto/editarNombre')
def adminProductoEditarNombre():
    id_producto = request.args.get('id_producto')
    nombre = request.args.get('nombre')
    if(actualizarNombreProducto(db, id_producto, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarDescripcion')
def adminProductoEditarDescripcion():
    id_producto = request.args.get('id_producto')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionProducto(db, id_producto, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarPrecio')
def adminProductoEditarPrecio():
    id_producto = request.args.get('id_producto')
    precio = request.args.get('precio')
    if(actualizarPrecioProducto(db, id_producto, precio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarUrlFoto')
def adminProductoEditarUrlFoto():
    id_producto = request.args.get('id_producto')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoProducto(db, id_producto, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarDisponible')
def adminProductoEditarDisponible():
    id_producto = request.args.get('id_producto')
    disponible = request.args.get('disponible')
    if(actualizarDisponibleProducto(db, id_producto, disponible)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#--------------------------------------------- Servicio ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
@app.route('/admin/servicio', methods = ["GET", "POST"])
def adminServicio():

    if request.method == "POST":
        id_emprendimiento = request.form.get("id_emprendimiento")
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        url_foto = request.form.get("url_foto")
        disponible = request.form.get("disponible")

        objeto_servicio = servicio(0, id_emprendimiento, nombre, descripcion, precio,  url_foto, disponible)
        res = insertarservicio(db,objeto_servicio)
        lista_servicio = mostrarservicio(db)
        return render_template("admin-servicio.html", lista_servicio = lista_servicio)

    else:
        lista_servicio = mostrarServicio(db)
        return render_template("admin-servicio.html", lista_servicio = lista_servicio)

@app.route('/admin/servicio/editarNombre')
def adminServicioEditarNombre():
    id_servicio = request.args.get('id_servicio')
    nombre = request.args.get('nombre')
    if(actualizarNombreServicio(db, id_servicio, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarDescripcion')
def adminServicioEditarDescripcion():
    id_servicio = request.args.get('id_servicio')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionServicio(db, id_servicio, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarPrecio')
def adminServicioEditarPrecio():
    id_servicio = request.args.get('id_servicio')
    precio = request.args.get('precio')
    if(actualizarPrecioServicio(db, id_servicio, precio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarUrlFoto')
def adminServicioEditarUrlFoto():
    id_servicio = request.args.get('id_servicio')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoServicio(db, id_servicio, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarDisponible')
def adminServicioEditarDisponible():
    id_servicio = request.args.get('id_servicio')
    disponible = request.args.get('disponible')
    if(actualizarDisponibleServicio(db, id_servicio, disponible)):
        return jsonify("True")
    else:
        return jsonify("False")
