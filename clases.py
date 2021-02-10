# Emprendedor Categoría Emprendimiento
# Cliente Comentario
# Feria Producto Servicio

class Emprendedor:
    def __init__(self, id_emprendedor, nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto):
        self.id_emprendedor = id_emprendedor
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.departamento = departamento
        self.municipio = municipio
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contrasena = contrasena
        self.url_foto = url_foto

class Categoria:
    def __init__(self, id_categoria, nombre, descripcion, url_foto):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.url_foto = url_foto

class Emprendimiento:
    def __init__(self, id_emprendimiento, id_categoria, id_emprendedor, nombre, departamento, municipio, direccion, descripcion, url_foto, link_facebook, link_youtube, link_instagram, link_twitter):
        self.id_emprendimiento = id_emprendimiento
        self.id_categoria = id_categoria
        self.id_emprendedor = id_emprendedor
        self.nombre = nombre
        self.departamento = departamento
        self.municipio = municipio
        self.direccion = direccion
        self.descripcion = descripcion
        self.url_foto = url_foto
        self.link_facebook = link_facebook
        self.link_youtube = link_youtube
        self.link_instagram = link_instagram
        self.link_twitter = link_twitter

class Cliente:
    def __init__(self, id_cliente, nombre, apellido, cedula, departamento, municipio, direccion, telefono, correo, fecha_nacimiento, contrasena, url_foto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.departamento = departamento
        self.municipio = municipio
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contrasena =  contrasena
        self.url_foto = url_foto

class Comentario:
    def __init__(self, id_comentario, id_emprendimiento, id_cliente, comentario, valoración, fechahora):
        self.id_comentario = id_comentario
        self.id_emprendimiento = id_emprendimiento
        self.id_cliente = id_cliente
        self.comentario = comentario
        self.valoracion = valoración
        self.fechahora = fechahora

class Feria:
    def __init__(self, id_feria, id_emprendimiento, nombre, descripcion, departamento, municipio, direccion, fecha_inicio, fecha_fin, url_foto):
        self.id_feria = id_feria
        self.id_emprendimiento = id_emprendimiento
        self.nombre = nombre
        self.descripcion = descripcion
        self.departamento = departamento
        self.municipio = municipio
        self.direccion = direccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.url_foto = url_foto

class Producto:
    def __init__(self, id_producto, id_emprendimiento, nombre, descripcion, precio, url_foto, disponible):
        self.id_producto = id_producto
        self.id_emprendimiento = id_emprendimiento
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.url_foto = url_foto
        self.disponible = disponible

class Servicio:
    def __init__(self, id_servicio, id_emprendimiento, nombre, descripcion, precio, url_foto, disponible):
        self.id_servicio = id_servicio
        self.id_emprendimiento = id_emprendimiento
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.url_foto = url_foto
        self.disponible = disponible