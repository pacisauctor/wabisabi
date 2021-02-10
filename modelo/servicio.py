from clases import Servicio

### Mostrar

def mostrarServicio(db):
    rows = db.execute("SELECT * FROM servicio")
    servicio = []
    for row in rows:
        servicio.append(Servicio(row["id_servicio"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return servicio

### Buscar

def buscarServicioPorid_servicio(db, texto):
    rows = db.execute("SELECT * FROM servicio WHERE id_servicio=?", texto);
    servicio = []
    for row in rows:
        servicio.append(Servicio(row["id_servicio"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return servicio[0]

def buscarServiciosPorEmprendimiento(db, idemp):
    rows = db.execute("SELECT * FROM servicio WHERE id_emprendimiento=?", idemp);
    servicios = []
    for row in rows:
        servicios.append(Servicio(row["id_servicio"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return servicios

def buscarServicio(db, texto):
    rows = db.execute("SELECT * FROM servicio WHERE nombre LIKE '%:k%' OR adescripcion LIKE '%:k%' OR precio LIKE '%:k%' OR  disponible  LIKE '%:k%'" , k = texto);
    servicio = []
    for row in rows:
        servicio.append(Servicio(row["id_servicio"], row["id_emprendedor"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return servicio

### Actualizar

def actualizarNombreServicio(db, id_servicio, nombre):
    res = db.execute("UPDATE servicio SET nombre=? WHERE id_servicio=?", nombre , id_servicio)
    if res == 0:
        return False
    else:
        return True

def actualizarDescripcionServicio(db, id_servicio, descripcion):
    res = db.execute("UPDATE servicio SET descripcion=? WHERE id_servicio=?", descripcion , id_servicio)
    if res == 0:
        return False
    else:
        return True

def actualizarPrecioServicio(db, id_servicio, precio):
    res = db.execute("UPDATE servicio SET precio=? WHERE id_servicio=?", precio , id_servicio)
    if res == 0:
        return False
    else:
        return True

def actualizarUrlFotoServicio(db, id_servicio, url_foto):
    res = db.execute("UPDATE servicio SET url_foto=? WHERE id_servicio=?", url_foto , id_servicio)
    if res == 0:
        return False
    else:
        return True

def actualizarDisponibleServicio(db, id_servicio, disponible):
    res = db.execute("UPDATE servicio SET disponible=? WHERE id_servicio=?", disponible , id_servicio)
    if res == 0:
        return False
    else:
        return True

### Insertar

def insertarServicio(db, s):
    if type(s) != Servicio:
        return -1
    res = db.execute("INSERT INTO servicio  (id_emprendimiento, nombre, descripcion, precio, url_foto, disponible) VALUES (:idemp, :nomb,:descri, :precio, :urlFoto, :dispo) ",idemp = s.id_emprendimiento, nomb=s.nombre, descri=s.descripcion, precio=s.precio, urlFoto=s.url_foto, dispo=s.disponible)
    return res