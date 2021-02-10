from clases import Producto

### Mostrar

def mostrarProductos(db):
    rows = db.execute("SELECT * FROM producto")
    producto = []
    for row in rows:
        producto.append(Producto(row["id_producto"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return producto

### Buscar

def buscarProductoPorNombre_Producto(db, texto):
    rows = db.execute("SELECT * FROM producto WHERE nombre LIKE '%:k%' OR descripcion LIKE  '%:k%' OR  precio  LIKE '%:k%' OR disponible LIKE '%:k%'", k = texto);
    producto = []
    for row in rows:
        producto.append(Producto(row["id_producto"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return producto

def buscarProductoPorId(db, id_producto):
    rows = db.execute("SELECT * FROM producto  WHERE id_producto=:k", k = id_producto);
    producto = []
    for row in rows:
        producto.append(Producto(row["id_producto"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return producto[0]
    
def buscarProductosPorEmprendimiento(db, idemp):
    rows = db.execute("SELECT * FROM producto  WHERE id_emprendimiento=:k", k = idemp);
    productos = []
    for row in rows:
        productos.append(Producto(row["id_producto"], row["id_emprendimiento"], row["nombre"], row["descripcion"], row["precio"], row["url_foto"], row["disponible"]))
    return productos

 ### Actualizar

def actualizarNombreProducto(db, id_producto, nombre):
    res = db.execute("UPDATE producto SET nombre=? WHERE id_producto=?", nombre,id_producto)
    if res == 0:
        return False
    else:
        return True

def actualizarDescripcionProducto(db, id_producto, descripcion):
    res = db.execute("UPDATE producto SET descripcion=? WHERE id_producto=?", descripcion,id_producto)
    if res == 0:
        return False
    else:
        return True


def actualizarPrecioProducto(db, id_producto, precio):
    res = db.execute("UPDATE producto SET precio=? WHERE id_producto=?", precio, id_producto)
    if res == 0:
        return False
    else:
        return True

def actualizarUrlFotoProducto(db, id_producto, url_foto):
    res = db.execute("UPDATE producto SET url_foto=? WHERE id_producto = ?", url_foto, id_producto)
    if res == 0:
        return False
    else:
        return True

def actualizarDisponibleProducto(db, id_producto, disponible):
    res = db.execute("UPDATE producto SET disponible=? WHERE id_producto=?", disponible , id_producto)
    if res == 0:
        return False
    else:
        return True

### Insertar
def insertarProducto(db, pr):
    if type(pr) != Producto:
        return -1
    res = db.execute("INSERT INTO producto (id_emprendimiento, nombre, descripcion, precio, url_foto, disponible) VALUES (:idemp, :nomb, :descri, :precio, :urlFoto, :disponible) ",idemp = pr.id_emprendimiento, nomb=pr.nombre, descri=pr.descripcion, precio=pr.precio, urlFoto=pr.url_foto, disponible=pr.disponible)
    return res