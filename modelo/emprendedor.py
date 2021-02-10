from clases import Emprendedor
from werkzeug.security import check_password_hash, generate_password_hash
#1. Emprendedor

def mostrarEmprendedores(db):
    rows = db.execute("SELECT * FROM emprendedor")
    emprendedor = []
    for row in rows:
        emprendedor.append(Emprendedor(row["id_emprendedor"], row["nombre"], row["apellido"], row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return emprendedor

####################################################################################
def buscarEmprendedor(db, texto):
    rows = db.execute("SELECT * FROM emprendedor WHERE nombre LIK'%:k%'  OR apellido LIKE '%:k%' OR cedula LIKE '%:k%' OR departamento LIKE '%:k%' OR municipio LIKE '%:k%' OR direccion LIKE '%:k%' OR telefono LIKE '%:k%' OR correo LIKE '%:k%' OR fecha_nacimiento LIKE '%:k%'", k = texto);
    emprendedor = []
    for row in rows:
        emprendedor.append(Emprendedor(row["id_emprendedor"], row["nombre"], row["apellido"], row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return emprendedor

def buscarEmprendedorPorId(db, id_emprendedor):
    rows = db.execute("SELECT * FROM emprendedor WHERE id_emprendedor=:k", k = id_emprendedor);
    emprendedor = []
    for row in rows:
        emprendedor.append(Emprendedor(row["id_emprendedor"], row["nombre"], row["apellido"], row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return emprendedor[0]

def inciarSesionEmprendedor(db, correo, contrasena):
    rows = db.execute("SELECT * FROM emprendedor WHERE correo=:k", k = correo);
    if(len(rows) == 0):
        return -1
    else:
        passBD = rows[0]["contrasena"]
        if check_password_hash(contrasena, passBD):
            return -1
        else:
            return rows[0]

#################################################################################### dpto, mun, foto
def actualizarNombreEmprendedor(db, id_emprendedor, nombre):
    res = db.execute("UPDATE emprendedor SET nombre=? WHERE id_emprendedor=?", nombre, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarApellidoEmprendedor(db, id_emprendedor, apellido):
    res = db.execute("UPDATE emprendedor SET apellido=? WHERE id_emprendedor=?", apellido, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarCedulaEmprendedor(db, id_emprendedor, cedula):
    res = db.execute("UPDATE emprendedor SET cedula=? WHERE id_emprendedor=?", cedula, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarDepartamentoEmprendedor(db, id_emprendedor, departamento):
    res = db.execute("UPDATE emprendedor SET departamento=? WHERE id_emprendedor=?", departamento, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarMunicipioEmprendedor(db, id_emprendedor, municipio):
    res = db.execute("UPDATE emprendedor SET municipio=? WHERE id_emprendedor=?", municipio, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarDireccionEmprendedor(db, id_emprendedor, direccion):
    res = db.execute("UPDATE emprendedor SET direccion=? WHERE id_emprendedor=?", direccion , id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarTelefonoEmprendedor(db, id_emprendedor, telefono):
    res = db.execute("UPDATE emprendedor SET telefono=? WHERE id_emprendedor=?", telefono, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarCorreoEmprendedor(db, id_emprendedor, correo):
    res = db.execute("UPDATE emprendedor SET correo=? WHERE id_emprendedor=?", correo , id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarFechaNacEmprendedor(db, id_emprendedor, fecha_nacimiento):
    res = db.execute("UPDATE emprendedor SET fecha_nacimiento=? WHERE id_emprendedor=?", fecha_nacimiento, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarContrasenaEmprendedor(db, id_emprendedor, contrasena):
    print("---------------" + str(contrasena) + "----------------")
    res = db.execute("UPDATE emprendedor SET contrasena=? WHERE id_emprendedor=?", generate_password_hash(contrasena), id_emprendedor)
    if res == 0:
        return False
    else:
        return True

def actualizarUrlFotoEmprendedor(db, id_emprendedor, url_foto):
    res = db.execute("UPDATE emprendedor SET url_foto=? WHERE id_emprendedor=?", url_foto, id_emprendedor)
    if res == 0:
        return False
    else:
        return True

###########################################################################################
def insertarEmprendedor(db, e):
    if type(e) != Emprendedor:
        return -1
    res = db.execute("INSERT INTO emprendedor (nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto) VALUES (:nomb,:apell,:ced,:dpto,:mun,:direccion,:tel,:mail,:fnac,:contra,:urlFoto) ", nomb=e.nombre, apell=e.apellido, ced =e.cedula, dpto=e.departamento, mun=e.municipio, direccion=e.direccion, tel=e.telefono, mail=e.correo, fnac=e.fecha_nacimiento, contra=generate_password_hash(e.contrasena), urlFoto=e.url_foto)
    return res