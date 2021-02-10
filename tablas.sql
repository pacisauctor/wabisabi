/*
1. Emprendedor
2. categoria
3. emprendimiento
4. Cliente
5. Comentario
6. Feria
7. Producto
8. servicio
*/
CREATE TABLE emprendedor(
    id_emprendedor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    cedula TEXT NOT NULL,
    departamento TEXT NOT NULL,
    municipio TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono INTEGER,
    correo TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    url_foto TEXT
);

CREATE TABLE categoria(
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    url_foto TEXT
);

CREATE TABLE emprendimiento (
    id_emprendimiento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_emprendedor INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    departamento TEXT NOT NULL,
    municipio TEXT NOT NULL,
    direccion TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    url_foto TEXT,
    link_facebook TEXT,
    link_youtube TEXT,
    link_instagram TEXT,
    link_twitter TEXT,

    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
    FOREIGN KEY (id_emprendedor) REFERENCES emprendedor(id_emprendedor)
);

CREATE TABLE cliente(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    cedula TEXT NOT NULL,
    departamento TEXT NOT NULL,
    municipio TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono INTEGER,
    correo TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    url_foto TEXT
);

CREATE TABLE comentario(
    id_comentario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_emprendimiento INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    comentario TEXT NOT NULL,
    valoracion TEXT NOT NULL,
    fechahora DATETIME NOT NULL,

    FOREIGN KEY (id_emprendimiento) REFERENCES emprendimiento(id_emprendimiento),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE feria(
    id_feria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_emprendimiento INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    departamento TEXT NOT NULL,
    municipio TEXT NOT NULL,
    direccion TEXT NOT NULL,
    fecha_inicio INTEGER NOT NULL,
    fecha_fin INTEGER NOT NULL,
    url_foto TEXT,
    FOREIGN KEY (id_emprendimiento) REFERENCES emprendimiento(id_emprendimiento)
);

CREATE TABLE producto(
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_emprendimiento INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL,
    url_foto TEXT NOT NULL,
    disponible INTEGER NOT NULL,
    FOREIGN KEY (id_emprendimiento) REFERENCES emprendimiento(id_emprendimiento)
);

CREATE TABLE servicio(
    id_servicio INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_emprendimiento INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL,
    url_foto TEXT NOT NULL,
    disponible INTEGER NOT NULL,

    FOREIGN KEY (id_emprendimiento) REFERENCES emprendimiento(id_emprendimiento)
);


SELECT e.*, c.nombre as nombre_categoria FROM emprendimiento e
INNER JOIN categoria c on e.id_categoria = c.id_categoria