from clases import Categoria

#2.Categoria

### Mostrar
def mostrarCategorias(db):
    rows = db.execute("SELECT * FROM categoria")
    categoria = []
    for row in rows:
        categoria.append(Categoria(row["id_categoria"], row["nombre"],
        row["descripcion"], row["url_foto"]))
    return categoria


### Buscar
def buscarCategoriaPorNombre(db, texto):
    rows = db.execute("SELECT * FROM categoria WHERE nombre LIKE '%:k%' OR descripcion LIKE'%:k%'", K = texto);
    categoria = []
    for row in rows:
        categoria.append(Categoria(row["id_categoria"], row["nombre"], row["descripcion"], row["url_foto"]))
    return categoria

def buscarCategoriaPorId(db, id_categoria):
    rows = db.execute("SELECT * FROM categoria  WHERE id_categoria=:k", k = id_categoria);
    categoria = []
    for row in rows:
        categoria.append(Categoria(row["id_categoria"], row["nombre"], row["descripcion"], row["url_foto"]))
    return categoria[0]


### Actualizar
def actualizarNombreCategoria(db, id_categoria, nombre):
    res = db.execute("UPDATE categoria SET nombre=? WHERE id_categoria=?",
    nombre , id_categoria)
    if res == 0:
        return False
    else:
        return True

def actualizarDescripcionCategoria(db, id_categoria, descripcion):
    res = db.execute("UPDATE categoria SET descripcion=? WHERE id_categoria=?", descripcion , id_categoria)
    if res == 0:
        return False
    else:
        return True

def actualizarUrlFotoCategoria(db, id_categoria, url_foto):
    res = db.execute("UPDATE categoria SET url_foto=? WHERE id_categoria=?", url_foto, id_categoria)
    if res == 0:
        return False
    else:
        return True

### Insertar
def insertarCategoria(db, c):
    if type(c) != Categoria:
        return -1
    res = db.execute("INSERT INTO categoria (nombre, descripcion, url_foto) VALUES (:nomb,:descripcion,:urlFoto) ",
    nomb=c.nombre, descripcion=c.descripcion, urlFoto=c.url_foto)
    return res