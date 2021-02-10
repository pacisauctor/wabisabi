from clases import Emprendimiento
# 3. Emprendimiento

# Mostrar +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def mostrarEmprendimientos(db):
    rows = db.execute("SELECT * FROM emprendimiento")
    emprendimiento = []
    for row in rows:
        emprendimiento.append(Emprendimiento(row["id_emprendimiento"], row["id_categoria"], row["id_emprendedor"], row["nombre"], row["departamento"], row["municipio"], row["direccion"], row["descripcion"], row["url_foto"], row["link_facebook"], row["link_youtube"], row["link_instagram"], row["link_twitter"]))
    return emprendimiento


def mostrarEmprendimientosMejorValorados(db):
    rows = db.execute('''
        SELECT ed.id_emprendimiento, ed.nombre, ed.departamento, ed.municipio, ed.url_foto, e.nombre   AS nombreEmp, e.apellido AS apellidoEmp, AVG(c.valoracion) as Valoracion
        FROM   emprendimiento ed
        INNER JOIN emprendedor e ON ed.id_emprendedor = e.id_emprendedor
        INNER JOIN comentario c ON c.id_emprendimiento = ed.id_emprendimiento
        GROUP BY ed.id_emprendimiento, ed.nombre, ed.departamento, ed.municipio, ed.url_foto, nombreEmp, apellidoEmp
        ORDER BY Valoracion DESC
        LIMIT  5;
    ''')
    return rows

def mostrarEmprendimientosPorCategoria(db, idcat):
    rows = db.execute("SELECT * FROM emprendimiento WHERE id_categoria=:idcat", idcat = idcat)
    emprendimientos = []
    for row in rows:
        emprendimientos.append(Emprendimiento(row["id_emprendimiento"], row["id_categoria"], row["id_emprendedor"], row["nombre"], row["departamento"], row["municipio"], row["direccion"], row["descripcion"], row["url_foto"], row["link_facebook"], row["link_youtube"], row["link_instagram"], row["link_twitter"]))
    return emprendimientos


def mostrarResumen(db, idemp):
    c = db.execute('''SELECT AVG(c.valoracion) AS valoracionPromedio, COUNT(c.id_comentario) AS numeroComentarios
                                FROM emprendimiento e
                                INNER JOIN comentario c ON e.id_emprendimiento = c.id_emprendimiento
                                WHERE e.id_emprendimiento = :k''', k = idemp)
    f = db.execute('''SELECT COUNT(f.id_feria) as cantidadFerias FROM emprendimiento e
                                INNER JOIN feria f ON f.id_emprendimiento = e.id_emprendimiento
                                WHERE e.id_emprendimiento = :k''', k = idemp)
    p = db.execute('''SELECT COUNT(p.id_producto) as cantidadProductos FROM emprendimiento e
                                INNER JOIN producto p ON p.id_emprendimiento = e.id_emprendimiento
                                WHERE e.id_emprendimiento = :k''', k = idemp)
    s = db.execute('''SELECT COUNT(s.id_servicio) as cantidadServicios FROM emprendimiento e
                                INNER JOIN servicio s ON s.id_emprendimiento = e.id_emprendimiento
                                WHERE e.id_emprendimiento = :k''', k = idemp)

    diccionario = {
        'valoracionPromedio': c[0]['valoracionPromedio'],
        'numeroComentarios': c[0]['numeroComentarios'],
        'cantidadFerias' : f[0]['cantidadFerias'],
        'cantidadProductos' : p[0]['cantidadProductos'],
        'cantidadServicios' : s[0]['cantidadServicios']
    }
    return diccionario

def mostrarEmprendimientosByIdEmp(db,idemprendedor):
    rows = db.execute(''' SELECT e.*, c.nombre as nombreCat FROM emprendimiento e
                        INNER JOIN categoria c ON c.id_categoria = e.id_categoria
                        WHERE e.id_emprendedor = :k''', k = idemprendedor);
    return rows

# Buscar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def buscarEmprendimiento(db, texto):
    rows = db.execute(f'''SELECT * FROM emprendimiento WHERE nombre LIKE '%{texto}%' OR departamento LIKE '%{texto}%' OR municipio LIKE '%{texto}%' OR direccion LIKE '%{texto}%' OR descripcion LIKE '%{texto}%' ''');
    emprendimiento = []
    for row in rows:
        emprendimiento.append(Emprendimiento(row["id_emprendimiento"], row["id_categoria"], row["id_emprendedor"], row["nombre"], row["departamento"], row["municipio"], row["direccion"], row["descripcion"], row["url_foto"], row["link_facebook"], row["link_youtube"], row["link_instagram"], row["link_twitter"]))
    return emprendimiento

def buscarEmprendimientoPorId(db, id_emprendimiento):
    rows = db.execute("SELECT * FROM emprendimiento WHERE id_emprendimiento=:k", k = id_emprendimiento);
    emprendimiento = []
    for row in rows:
        emprendimiento.append(Emprendimiento(row["id_emprendimiento"], row["id_categoria"], row["id_emprendedor"], row["nombre"], row["departamento"], row["municipio"], row["direccion"], row["descripcion"], row["url_foto"], row["link_facebook"], row["link_youtube"], row["link_instagram"], row["link_twitter"]))
    return emprendimiento[0]


# Actualizar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1-Nombre
def actualizarNombreEmprendimiento(db, id_emprendimiento, nombre):
    res = db.execute("UPDATE emprendimiento SET nombre=? WHERE id_emprendimiento=?", nombre, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 1.5 categoria
def actualizarCategoriaEmprendimiento(db, id_emprendimiento, id_categoria):
    res = db.execute("UPDATE emprendimiento SET id_categoria=? WHERE id_emprendimiento=?", id_categoria, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True
# 2-Departamento
def actualizarDepartamentoEmprendimiento(db, id_emprendimiento, departamento):
    res = db.execute("UPDATE emprendimiento SET departamento=? WHERE id_emprendimiento=?", departamento, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 3-Municipio
def actualizarMunicipioEmprendimiento(db, id_emprendimiento, municipio):
    res = db.execute("UPDATE emprendimiento SET municipio=? WHERE id_emprendimiento=?", municipio, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 4-Direccion
def actualizarDireccionEmprendimiento(db, id_emprendimiento, direccion):
    res = db.execute("UPDATE emprendimiento SET direccion=? WHERE id_emprendimiento=?", direccion, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 5-Descripción
def actualizarDescripcionEmprendimiento(db, id_emprendimiento, descripcion):
    res = db.execute("UPDATE emprendimiento SET descripcion=? WHERE id_emprendimiento=?", descripcion, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 6-Url_foto
def actualizarUrlFotoEmprendimiento(db, id_emprendimiento, url_foto):
    res = db.execute("UPDATE emprendimiento SET url_foto=? WHERE id_emprendimiento=?", url_foto, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 7-Link Facebook
def actualizarLinkFacebookEmprendimiento(db, id_emprendimiento, link_facebook):
    res = db.execute("UPDATE emprendimiento SET link_facebook=? WHERE id_emprendimiento=?", link_facebook, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 8-Link Youtube
def actualizarLinkYoutubeEmprendimiento(db, id_emprendimiento, link_youtube):
    res = db.execute("UPDATE emprendimiento SET link_youtube=? WHERE id_emprendimiento=?", link_youtube, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 9-Link Instagram
def actualizarLinkInstagramEmprendimiento(db, id_emprendimiento, link_instagram):
    res = db.execute("UPDATE emprendimiento SET link_instagram=? WHERE id_emprendimiento=?", link_instagram, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# 10-Link Twitter
def actualizarLinkTwitterEmprendimiento(db, id_emprendimiento, link_twitter):
    res = db.execute("UPDATE emprendimiento SET link_twitter=? WHERE id_emprendimiento=?", link_twitter, id_emprendimiento)
    if res == 0:
        return False
    else:
        return True

# Insertar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def insertarEmprendimiento(db, em):
    if type(em) != Emprendimiento:
        return -1
    res = db.execute("INSERT INTO emprendimiento (id_emprendedor, id_categoria, nombre, departamento, municipio, direccion, descripcion, url_foto, link_facebook, link_youtube, link_instagram, link_twitter) VALUES (:idemprendedor, :idcat, :nomb, :dpto, :mun, :direccion, :descripcion, :urlfoto, :linkface, :linkyoutube, :linkinsta, :linktw)",idemprendedor=em.id_emprendedor, idcat = em.id_categoria, nomb=em.nombre, dpto=em.departamento, mun=em.municipio, direccion=em.direccion, descripcion=em.descripcion, urlfoto=em.url_foto, linkface=em.link_facebook, linkyoutube=em.link_youtube, linkinsta = em.link_instagram, linktw=em.link_twitter)
    return res