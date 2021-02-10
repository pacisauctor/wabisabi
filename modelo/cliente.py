from clases import Cliente
from werkzeug.security import check_password_hash, generate_password_hash
# 4. Cliente

### Mostrar
def mostrarClientes(db):
    rows = db.execute("SELECT * FROM cliente")
    cliente = []
    for row in rows:
        cliente.append(Cliente(row["id_cliente"], row["nombre"], row["apellido"], row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return cliente

### Buscar
def buscarClientePorNombre_cliente(db, texto):
    rows = db.execute("SELECT * FROM cliente WHERE nombre LIKE '%:k%' OR apellido LIKE  '%:k%' OR cedula LIKE  '%:k%' OR departamento LIKE  '%:k%' OR direccion LIKE '%:k%' OR telefono LIKE '%:k%'", k = texto);
    cliente = []
    for row in rows:
        cliente.append(Cliente(row["id_cliente"], row["nombre"], row["apellido"], row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return cliente

def buscarClientePorId(db, id_cliente):
    rows = db.execute("SELECT * FROM cliente WHERE id_cliente=:k", k = id_cliente);
    cliente = []
    for row in rows:
        cliente.append(Cliente(row["id_cliente"], row["nombre"], row["apellido"] , row["cedula"], row["departamento"], row["municipio"], row["direccion"], row["telefono"], row["correo"], row["fecha_nacimiento"], row["contrasena"], row["url_foto"]))
    return cliente[0]



def iniciarSesionCliente(db, correo, contrasena):
    rows = db.execute("SELECT * FROM cliente WHERE correo=:k", k = correo);
    if(len(rows) == 0):
        return -1
    else:
        passBD = rows[0]["contrasena"]
        if not check_password_hash(contrasena, passBD):
            return -1
        else:
            return rows[0]
### Actualizar

def actualizarNombreCliente(db, id_cliente, nombre):
    res = db.execute("UPDATE cliente SET nombre=? WHERE id_cliente=?", nombre , id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarApellidoCliente(db, id_cliente, apellido):
    res = db.execute("UPDATE cliente SET apellido=? WHERE id_cliente=?", apellido, id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarCedulaCliente(db, id_cliente, cedula):
    res = db.execute("UPDATE cliente SET cedula=? WHERE id_cliente=?", cedula, id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarDepartamentoCliente(db, id_cliente, departamento):
    res = db.execute("UPDATE cliente SET departamento=? WHERE id_cliente=?", departamento, id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarMunicipioCliente(db, id_cliente, municipio):
    res = db.execute("UPDATE cliente SET municipio=? WHERE id_cliente=?", municipio, id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarDireccionCliente(db, id_cliente, direccion):
    res = db.execute("UPDATE cliente SET direccion=? WHERE id_cliente=?", direccion , id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarTelefonoCliente(db, id_cliente, telefono):
    res = db.execute("UPDATE cliente SET telefono=? WHERE id_cliente=?", telefono , id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarCorreoCliente(db, id_cliente, correo):
    res = db.execute("UPDATE cliente SET correo=? WHERE id_cliente=?", correo , id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarFechaNacCliente(db, id_cliente, fecha_nacimiento):
    res = db.execute("UPDATE cliente SET fecha_nacimiento=? WHERE id_cliente=?", fecha_nacimiento, id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarContrasenaCliente(db, id_cliente, contrasena):
    res = db.execute("UPDATE cliente SET contrasena=? WHERE id_cliente=?", generate_password_hash(contrasena) , id_cliente)
    if res == 0:
        return False
    else:
        return True

def actualizarUrl_FotoCliente(db, id_cliente, url_foto):
    res = db.execute("UPDATE cliente SET url_foto=? WHERE id_cliente=?", url_foto , id_cliente)
    if res == 0:
        return False
    else:
        return True

### Insertar

def insertarCliente(db, cl):
    if type(cl) != Cliente:
        return -1
    res = db.execute("INSERT INTO cliente (nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto) VALUES (:nomb, :apelli, :cedu, :depa, :muni, :dire, :telf, :correo,  :fecha_nac,:contra, :urlFoto) ", nomb=cl.nombre, apelli=cl.apellido, cedu=cl.cedula, depa=cl.departamento, muni=cl.municipio,dire= cl.direccion, telf=cl.telefono , correo=cl.correo, fecha_nac=cl.fecha_nacimiento, contra=cl.contrasena, urlFoto=cl.url_foto)
    return res