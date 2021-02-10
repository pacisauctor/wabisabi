from clases import Comentario
# 5. Comentario

# Mostrar +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def mostrarComentarios(db):
    rows = db.execute("SELECT * FROM comentario")
    comentario = []
    for row in rows:
        comentario.append(Comentario(row["id_comentario"], row["id_emprendimiento"],
                                     row["id_cliente"], row["comentario"], row["valoracion"], row["fechahora"]))
    return comentario


def mostrarComentarioPorEmprendimiento(db, id_emprendimiento):
    rows = db.execute('''SELECT c.*, cl.nombre as nombreCl, cl.apellido as apellidoCl FROM comentario c
                        INNER JOIN cliente cl ON c.id_cliente = cl.id_cliente
                        WHERE id_emprendimiento = ?''', id_emprendimiento)
    return rows

# Actualizar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Comentario


def actualizarContenidoComentario(db, id_comentario, comentario):
    res = db.execute(
        "UPDATE comentario SET comentario=? WHERE id_comentario=?", comentario, id_comentario)
    if res == 0:
        return False
    else:
        return True

# Valoración


def actualizarValoracionComentario(db, id_comentario, valoracion):
    res = db.execute(
        "UPDATE comentario SET valoracion=? WHERE id_comentario=?", valoracion, id_comentario)
    if res == 0:
        return False
    else:
        return True

# Fecha y hora


def actualizarFechaHoraComentario(db, id_comentario, fechahora):
    res = db.execute(
        "UPDATE comentario SET fechahora=? WHERE id_comentario=?", fechahora, id_comentario)
    if res == 0:
        return False
    else:
        return True

# Insertar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def insertarComentario(db, co):
    if type(co) != Comentario:
        return -1
    res = db.execute("INSERT INTO comentario (id_emprendimiento, id_cliente, comentario, valoracion, fechahora) VALUES (:idemp, :idcli, :com, :val, datetime('now','localtime'))",
                     idemp=co.id_emprendimiento, idcli=co.id_cliente, com=co.comentario, val=co.valoracion)
    return res
