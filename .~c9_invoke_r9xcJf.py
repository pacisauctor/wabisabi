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
from modelo.comentario import *
from clases import *
from helpers import *

db = SQL("sqlite:///wabisabi.db")
app = Flask(__name__)
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
def index():
    if not session:
        topValoracion = mostrarEmprendimientosMejorValorados(db)
        return render_template("cliente-index.html", topValoracion = topValoracion)
    if(session["tipo"] == "cliente"):
        topValoracion = mostrarEmprendimientosMejorValorados(db)
        return render_template("cliente-index.html", topValoracion = topValoracion)
    elif(session["tipo"] == "emprendedor"):
        return render_template("emprendedor-index.html")
    else:
        return redirect("/login")


@app.route('/cliente/contacto')
@app.route('/emprendedor/contacto')
def contacto():
   return render_template('contacto.html')

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
                flash("Contraseña/Correo incorrecto, intente otra vez.")
                return redirect(url_for("login"))
            else:
                session["user_id"] = res["id_cliente"]
                session["tipo"] = "cliente"
                return redirect("/")

        elif (tipo == "emprendedor"):
            res = inciarSesionEmprendedor(db, correo, contraseña)
            if(res == -1):
                flash("Contraseña/Correo incorrecto, intente otra vez.")
                return redirect(url_for("login"))
            else:
                session["user_id"] = res["id_emprendedor"]
                session["tipo"] = "emprendedor"
                return redirect("/")
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
    lista = mostrarEmprendimientosByIdEmp(db, session["user_id"])
    return render_template("emprendedor-emprendimiento.html", emprendimientos = lista)


@app.route("/emprendedor/ferias")
@login_required
def emprendedorFerias():
    ferias = mostrarFeria(db)
    return render_template("emprendedor-ferias.html", ferias = ferias)


#######################################cliente####################################################
@app.route("/cliente/emprendimientos")
def clienteEmprendimientos():
        lista_categorias = mostrarCategorias(db)
        
        return render_template("cliente-categorias.html", categorias = lista_categorias)

@app.route("/cliente/emprendimientoF/<int:idcat>")
def clienteEmprendimientoF(idcat):
        categoria = buscarCategoriaPorId(db, idcat)
        lista_emprendimientos = mostrarEmprendimientosPorCategoria(db, idcat)
        return render_template("cliente-emprendimientos.html", emprendimientos = lista_emprendimientos, categoria = categoria)


@app.route("/cliente/emprendimientos/<int:idemp>")
def clienteEmprendimiento(idemp):
    emprendimiento = buscarEmprendimientoPorId(db,idemp)
    categoria = buscarCategoriaPorId(db, emprendimiento.id_categoria)
    emprendedor = buscarEmprendedorPorId(db, emprendimiento.id_emprendedor)
    ferias = buscarFeriasPorEmprendimiento(db,idemp)
    productos = buscarProductosPorEmprendimiento(db, idemp)
    servicios = buscarServiciosPorEmprendimiento(db, idemp)
    comentarios = mostrarComentarioPorEmprendimiento(db,idemp)
    resumen = mostrarResumen(db, idemp)
    return render_template("cliente-emprendimiento.html", edto = emprendimiento, e = emprendedor, c = categoria, fs = ferias, ps= productos, ss = servicios, resumen = resumen, comentarios = comentarios)

@app.route("/cliente/ferias")
@login_required
def clienteFerias():
    ferias = mostrarFeria(db)
    return render_template("cliente-ferias.html", ferias = ferias)


@app.route("/cliente/perfil")
@login_required
def clientePerfil():
    id_cliente = session["user_id"]
    cliente_perfil = buscarClientePorId(db, id_cliente)
    return render_template("cliente-perfil.html", cliente_perfil =cliente_perfil)




#########################################################################################################
#                                           ADMINISTRACION                                              #
#########################################################################################################

@app.route('/admin')
def admin():
    session.clear()
    session["tipo"] = "admin"
    return render_template("administracion.html")

#-------------------------------------------------------------------------------------------------------#
#---------------------------------------------- Categoría ----------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

@app.route('/admin/categoria', methods = ["GET", "POST"])
def adminCategoria():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        url = request.form.get("url_foto")

        # esto es con respecto al constructor en clases.py
        objeto_categoria = Categoria(0, nombre, descripcion, url)
        res  = insertarCategoria(db,objeto_categoria)
        lista_categorias = mostrarCategorias(db)
        return render_template("admin-categoria.html", lista_categorias = lista_categorias)
    else:
        lista_categorias = mostrarCategorias(db)
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
    imagen = request.args.get("url_foto")
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
            lista_cliente = mostrarClientes(db)
            return render_template("admin-cliente.html", lista_cliente = lista_cliente)

    else:
        lista_cliente = mostrarClientes(db)
        return render_template("admin-cliente.html", lista_cliente = lista_cliente)

@app.route('/admin/cliente/editarNombre')
def adminClienteEditarNombre():
    idCliente = request.args.get('idCliente')
    nombre = request.args.get('nombre')
    if(actualizarNombreCliente(db, idCliente, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarApellido')
def adminClienteEditarApellido():
    idCliente = request.args.get('idCliente')
    apellido = request.args.get('apellido')
    if(actualizarApellidoCliente(db, idCliente, apellido)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarCedula')
def adminClienteEditarCedula():
    idCliente = request.args.get('idCliente')
    cedula = request.args.get('cedula')
    if(actualizarCedulaCliente(db, idCliente, cedula)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarDpto')
def adminClienteEditarDpto():
    idCliente = request.args.get('idCliente')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoCliente(db, idCliente, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarMunicipio')
def adminClienteEditarMunicipio():
    idCliente = request.args.get('idCliente')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioCliente(db, idCliente, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarDireccion')
def adminClienteEditarDireccion():
    idCliente = request.args.get('idCliente')
    direccion = request.args.get('direccion')
    if(actualizarDireccionCliente(db, idCliente, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarTel')
def adminClienteEditarTel():
    idCliente = request.args.get('idCliente')
    telefono = request.args.get('telefono')
    if(actualizarTelefonoCliente(db, idCliente, telefono)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarCorreo')
def adminClienteEditarCorreo():
    idCliente = request.args.get('idCliente')
    correo = request.args.get('correo')
    if(actualizarCorreoCliente(db, idCliente, correo)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarNac')
def adminClienteEditarNac():
    idCliente = request.args.get('idCliente')
    fechaNac = request.args.get('fecha_nacimiento')
    if(actualizarFechaNacCliente(db, idCliente, fechaNac)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarContra')
def adminClienteEditar():
    idCliente = request.args.get('idCliente')
    contra = request.args.get('contrasena')
    if(actualizarContrasenaCliente(db, idCliente, contra)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/cliente/editarImagen')
def adminClienteEditarImagen():
    idCliente = request.args.get('idCliente')
    imagen = request.args.get('url_foto')
    if(actualizarUrl_FotoCliente(db, idCliente, imagen)):
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
        res = insertarEmprendedor(db,objeto_emprendedor)
        if(autor == "user"):
            session["user_id"] = res
            session["tipo"] = "emprendedor"
            return redirect("/")
        else:
            lista_cliente = mostrarCliente(db)
            return render_template("admin-cliente.html", lista_cliente = lista_cliente)
    else:
       lista_emprendedor = mostrarEmprendedores(db)
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
    direccion = request.args.get('direccion')
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

@app.route('/admin/emprendedor/editarFechaNac')
def adminEmprendedorEditarFechaNac():
    idEmprendedor = request.args.get('idEmprendedor')
    fecha_nacimiento = request.args.get('fecha_nacimiento')
    if(actualizarFechaNacEmprendedor(db, idEmprendedor, fecha_nacimiento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendedor/editarContrasena')
def adminEmprendedorEditarContrasena():
    idEmprendedor = request.args.get('idEmprendedor')
    contrasena = request.args.get('contrasena')
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

    lista_categoria = mostrarCategorias(db)
    lista_emprendedores = mostrarEmprendedores(db)
    lista_emprendimiento = mostrarEmprendimientos(db)
    return render_template("admin-emprendimiento.html", lista_emprendimiento = lista_emprendimiento, emprendedores =  lista_emprendedores, categorias = lista_categoria )

@app.route('/admin/emprendimiento/editarNombre')
def adminEmprendimientoEditarNombre():
    idEmprendimiento = request.args.get('idEmprendimiento')
    nombre = request.args.get('nombre')
    if(actualizarNombreEmprendimiento(db, idEmprendimiento, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDepartamento')
def adminEmprendimientoEditarDepartamento():
    idEmprendimiento = request.args.get('idEmprendimiento')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoEmprendimiento(db, idEmprendimiento, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarMunicipio')
def adminEmprendimientoEditarMunicipio():
    idEmprendimiento = request.args.get('idEmprendimiento')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioEmprendimiento(db, idEmprendimiento, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDireccion')
def adminEmprendimientoEditarDireccion():
    idEmprendimiento = request.args.get('idEmprendimiento')
    direccion = request.args.get('direccion')
    if(actualizarDireccionEmprendimiento(db, idEmprendimiento, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarDescripcion')
def adminEmprendimientoEditarDescripcion():
    idEmprendimiento = request.args.get('idEmprendimiento')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionEmprendimiento(db, idEmprendimiento, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarUrlFoto')
def adminEmprendimientoEditarUrlFoto():
    idEmprendimiento = request.args.get('idEmprendimiento')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoEmprendimiento(db, idEmprendimiento, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkFacebook')
def adminEmprendimientoEditarLinkFacebook():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_facebook = request.args.get('link_facebook')
    if(actualizarLinkFacebookEmprendimiento(db, idEmprendimiento, link_facebook)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkYoutube')
def adminEmprendimientoEditarLinkYoutube():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_youtube = request.args.get('link_youtube')
    if(actualizarLinkYoutubeEmprendimiento(db, idEmprendimiento, link_youtube)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkInstagram')
def adminEmprendimientoEditarLinkInstagram():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_instagram = request.args.get('link_instagram')
    if(actualizarLinkInstagramEmprendimiento(db, idEmprendimiento, link_instagram)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/emprendimiento/editarLinkTwitter')
def adminEmprendimientoEditarLinkTwitter():
    idEmprendimiento = request.args.get('idEmprendimiento')
    link_twitter = request.args.get('link_twitter')
    if(actualizarLinkTwitterEmprendimiento(db, idEmprendimiento, link_twitter)):
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
    lista_emprendimientos = mostrarEmprendimientos(db)
    return render_template("admin-feria.html", lista_feria = lista_feria, emprendimientos = lista_emprendimientos)

@app.route('/admin/feria/editarNombre')
def adminFeriaEditarNombre():
    idFeria = request.args.get('idFeria')
    nombre = request.args.get('nombre')
    if(actualizarNombreFeria(db, idFeria, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDescripcion')
def adminFeriaEditarDescripcion():
    idFeria = request.args.get('idFeria')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionFeria(db, idFeria, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDepartamento')
def adminFeriaEditarDepartamento():
    idFeria = request.args.get('idFeria')
    departamento = request.args.get('departamento')
    if(actualizarDepartamentoFeria(db, idFeria, departamento)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarMunicipio')
def adminFeriaEditarMunicipio():
    idFeria = request.args.get('idFeria')
    municipio = request.args.get('municipio')
    if(actualizarMunicipioFeria(db, idFeria, municipio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarDireccion')
def adminFeriaEditarDireccion():
    idFeria = request.args.get('idFeria')
    direccion = request.args.get('direccion')
    if(actualizarDireccionFeria(db, idFeria, direccion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarFechaInicio')
def adminFeriaEditarFechaInicio():
    idFeria = request.args.get('idFeria')
    fecha_inicio = request.args.get('fecha_inicio')
    if(actualizarFechaInicioFeria(db, idFeria, fecha_inicio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarFechaFin')
def adminFeriaEditarFechaFin():
    idFeria = request.args.get('idFeria')
    fecha_fin = request.args.get('fecha_fin')
    if(actualizarFechaFinFeria(db, idFeria, fecha_fin)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/feria/editarUrlFoto')
def adminFeriaEditarUrlFoto():
    idFeria = request.args.get('idFeria')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoFeria(db, idFeria, url_foto)):
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

    lista_producto = mostrarProductos(db)
    lista_emprendimiento = mostrarEmprendimientos(db)
    return render_template("admin-producto.html", productos = lista_producto, emprendimientos = lista_emprendimiento)

@app.route('/admin/producto/editarNombre')
def adminProductoEditarNombre():
    idProducto = request.args.get('idProducto')
    nombre = request.args.get('nombre')
    if(actualizarNombreProducto(db, idProducto, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarDescripcion')
def adminProductoEditarDescripcion():
    idProducto = request.args.get('idProducto')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionProducto(db, idProducto, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarPrecio')
def adminProductoEditarPrecio():
    idProducto = request.args.get('idProducto')
    precio = request.args.get('precio')
    if(actualizarPrecioProducto(db, idProducto, precio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarUrlFoto')
def adminProductoEditarUrlFoto():
    idProducto = request.args.get('idProducto')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoProducto(db, idProducto, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/producto/editarDisponible')
def adminProductoEditarDisponible():
    idProducto = request.args.get('idProducto')
    disponible = request.args.get('disponible')
    if(actualizarDisponibleProducto(db, idProducto, disponible)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#--------------------------------------------- Servicio ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
@app.route('/admin/servicio', methods = ["GET", "POST"])
def adminServicio():
    if request.method =="POST":
        id_emprendimiento = request.form.get("id_emprendimiento")
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        url_foto = request.form.get("url_foto")
        disponible = request.form.get("disponible")

        objeto_servicio = Servicio(0, id_emprendimiento, nombre, descripcion, precio,  url_foto, disponible)
        res = insertarServicio(db,objeto_servicio)

    lista_emprendimiento = mostrarEmprendimientos(db)
    lista_servicio= mostrarServicio(db)
    return render_template("admin-servicio.html", lista_servicio = lista_servicio, emprendimientos = lista_emprendimiento)

############################ AL MENOS YA NO NOS DA ERROR PEROOOOOOOO NO SE AGREGA NADA ###################################################

@app.route('/admin/servicio/editarNombre')
def adminServicioEditarNombre():
    id_servicio = request.args.get('idServicio')
    nombre = request.args.get('nombre')
    if(actualizarNombreServicio(db, id_servicio, nombre)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarDescripcion')
def adminServicioEditarDescripcion():
    id_servicio = request.args.get('idServicio')
    descripcion = request.args.get('descripcion')
    if(actualizarDescripcionServicio(db, id_servicio, descripcion)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarPrecio')
def adminServicioEditarPrecio():
    id_servicio = request.args.get('idServicio')
    precio = request.args.get('precio')
    if(actualizarPrecioServicio(db, id_servicio, precio)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarUrlFoto')
def adminServicioEditarUrlFoto():
    id_servicio = request.args.get('idServicio')
    url_foto = request.args.get('url_foto')
    if(actualizarUrlFotoServicio(db, id_servicio, url_foto)):
        return jsonify("True")
    else:
        return jsonify("False")

@app.route('/admin/servicio/editarDisponible')
def adminServicioEditarDisponible():
    id_servicio = request.args.get('idServicio')
    disponible = request.args.get('disponible')
    if(actualizarDisponibleServicio(db, id_servicio, disponible)):
        return jsonify("True")
    else:
        return jsonify("False")

#-------------------------------------------------------------------------------------------------------#
#--------------------------------------------- Comentario ------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
@app.route('/admin/comentario', methods = ["GET", "POST"])
@login_required
def adminComentario():
    if request.method =="POST":
        autor = request.form.get('autor')
        id_emprendimiento = request.form.get("id_emprendimiento")
        id_cliente = request.form.get("id_cliente")
        comentario = request.form.get("comentario")
        valoracion = request.form.get("valoracion")
        
        objeto_comentario = Comentario(0,id_emprendimiento, id_cliente, comentario, valoracion, "")

        res = insertarComentario(db,objeto_comentario)
        if(autor == "cliente"):
            return redirect('/cliente/emprendimientos/' + str(id_emprendimiento))

    lista_comentario = mostrarComentarios(db)
    lista_emprendimiento = mostrarEmprendimientos(db)
    lista_clientes = mostrarClientes(db)
    return render_template("admin-comentario.html", comentarios = lista_comentario, emprendimientos = lista_emprendimiento, clientes = lista_clientes)
