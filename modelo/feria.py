from clases import Feria
# 6. Feria

# Mostrar +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def mostrarFeria(db):
    rows = db.execute("SELECT * FROM feria")
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria

def mostrarFeriasFuturas(db):
    rows = db.execute("SELECT * FROM feria WHERE fecha_inicio > DATE('now') ORDER BY fecha_inicio ASC;")
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria

def mostrarFeriasHoy(db):
    rows = db.execute("SELECT * FROM feria WHERE fecha_inicio = DATE('now') OR (fecha_fin > DATE('now') AND fecha_inicio < DATE('now'));")
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria
def mostrarFeriasPasadas(db):
    rows = db.execute("SELECT * FROM feria WHERE fecha_fin < DATE('now') ORDER BY fecha_inicio DESC;")
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria

# Buscar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def buscarFeria(db, texto):
    rows = db.execute("SELECT * FROM feria WHERE nombre LIKE '%:k%' OR descripcion LIKE '%:k%' OR departamento LIKE '%:k%' OR municipio LIKE '%:k%' OR direccion LIKE '%:k%' OR fecha_inicio LIKE '%:k%' OR fecha_fin LIKE '%:k%'", k = texto);
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria

def buscarFeriaPorId(db, id_feria):
    rows = db.execute("SELECT * FROM feria WHERE id_feria=:k", k = id_feria);
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria[0]

def buscarFeriasPorEmprendimiento(db, id_emprendimiento):
    rows = db.execute("SELECT * FROM feria WHERE id_emprendimiento=:k", k = id_emprendimiento);
    feria = []
    for row in rows:
        feria.append(Feria(row["id_feria"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["departamento"], row["municipio"], row["direccion"], row["fecha_inicio"], row["fecha_fin"], row["url_foto"]))
    return feria

def buscarFeriasPorEmprendedor(db, id_emprendedor):
    rows = db.execute(''' SELECT f.*, e2.id_emprendedor FROM feria f
                            INNER JOIN emprendimiento e ON e.id_emprendimiento = f.id_emprendimiento
                            INNER JOIN emprendedor e2 ON e2.id_emprendedor = e.id_emprendedor
                            WHERE e2.id_emprendedor=:k''', k = id_emprendedor);
    return rows
# Actualizar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Nombre
def actualizarNombreFeria(db, id_feria, nombre):
    res = db.execute("UPDATE feria SET nombre=? WHERE id_feria=?", nombre, id_feria)
    if res == 0:
        return False
    else:
        return True


def actualizarIdEmprendFeria(db, id_feria, id_emprendimiento):
    res = db.execute("UPDATE feria SET id_emprendimiento=? WHERE id_feria=?", id_emprendimiento, id_feria)
    if res == 0:
        return False
    else:
        return True
# Descripcion
def actualizarDescripcionFeria(db, id_feria, descripcion):
    res = db.execute("UPDATE feria SET descripcion=? WHERE id_feria=?", descripcion, id_feria)
    if res == 0:
        return False
    else:
        return True

# Departamento
def actualizarDepartamentoFeria(db, id_feria, departamento):
    res = db.execute("UPDATE feria SET departamento=? WHERE id_feria=?", departamento, id_feria)
    if res == 0:
        return False
# Municipio
def actualizarMunicipioFeria(db, id_feria, municipio):
    res = db.execute("UPDATE feria SET municipio=? WHERE id_feria=?", municipio, id_feria)
    if res == 0:
        return False
    else:
        return True

# Direccion
def actualizarDireccionFeria(db, id_feria, direccion):
    res = db.execute("UPDATE feria SET direccion=? WHERE id_feria=?", direccion, id_feria)
    if res == 0:
        return False
    else:
        return True

# Fecha inicio
def actualizarFechaInicioFeria(db, id_feria, fecha_inicio):
    res = db.execute("UPDATE feria SET fecha_inicio=? WHERE id_feria=?", fecha_inicio, id_feria)
    if res == 0:
        return False
    else:
        return True

# Fecha fin
def actualizarFechaFinFeria(db, id_feria, fecha_fin):
    res = db.execute("UPDATE feria SET fecha_fin=? WHERE id_feria=?", fecha_fin, id_feria)
    if res == 0:
        return False
    else:
        return True

# Url foto
def actualizarUrlFotoFeria(db, id_feria, url_foto):
    res = db.execute("UPDATE feria SET url_foto=? WHERE id_feria=?", url_foto, id_feria)
    if res == 0:
        return False
    else:
        return True

# Insertar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def insertarFeria(db, f):
    if type(f) != Feria:
        return -1
    res = db.execute("INSERT INTO feria (id_emprendimiento, nombre, descripcion, departamento, municipio, direccion, fecha_inicio, fecha_fin, url_foto) VALUES (:idemp, :nomb, :descripcion, :dpto, :mun, :direccion, :fechainicio, :fechafin, :urlfoto)", idemp=f.id_emprendimiento, nomb=f.nombre, descripcion=f.descripcion, dpto=f.departamento, mun=f.municipio, direccion=f.direccion, fechainicio=f.fecha_inicio, fechafin=f.fecha_fin, urlfoto=f.url_foto)
    return res