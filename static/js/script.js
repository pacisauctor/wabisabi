function admin(iddiv){
    var i;
    var lista = document.getElementsByClassName("administracion");
    for(i = 0; i < lista.length; i++){
        lista[i].style.display = "none";
    }
    document.getElementById(iddiv).style.display = "block";
}
function realizarPeticion(ruta, nombreParam, valoresParam, mensaje){
    var xmlHTTP = new XMLHttpRequest();
    var url = ruta+"?";
    var cantidadParametros = nombreParam.length;
    console.log(cantidadParametros);
    for (var i = 0; i < cantidadParametros; i++){
        if(i == cantidadParametros - 1){
            url += nombreParam[i] + "=" + valoresParam[i];
        }
        else{
            url += nombreParam[i] + "=" + valoresParam[i] + "&";
        }
    }

    xmlHTTP.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var res = JSON.parse(this.responseText);
                console.log(res);

                location.href= url.split("/",3).join('/');
            }
    };
    xmlHTTP.open("GET", url, true);
    xmlHTTP.send();

}
function editarCategoriaNombre(idCategoria){
    var nombre = prompt("Ingrese el nuevo nombre: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCategoria', 'nombre'];
        var valoresParam = [idCategoria, nombre];
        var url = "/admin/categoria/editarNombre";
        realizarPeticion(url,nombreParam,valoresParam,"Edición Exitosa!");

    }
}

function editarCategoriaDescripcion(idCategoria){
    var descripcion = prompt("Ingrese la nueva descripcion: ");
    if(descripcion == "" || descripcion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCategoria', 'descripcion'];
        var valoresParam = [idCategoria, descripcion];
        var url = "/admin/categoria/editarDescripcion";
        realizarPeticion(url,nombreParam,valoresParam,"Edición Exitosa!");
    }
}

function editarCategoriaURL_Foto(idCategoria){
    var url_foto = prompt("Ingrese la nueva URL de la imagen: ")
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCategoria', 'url_foto'];
        var valoresParam = [idCategoria, url_foto];
        var url = "/admin/categoria/editarImagen";
        realizarPeticion(url,nombreParam,valoresParam,"Edición Exitosa!");
    }
}

/*
###################################################################################################################
###########################################Cliente ##########################################################
###################################################################################################################
*/

function editarClienteNombre(idCliente){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'nombre'];
        var valoresParam = [idCliente, nombre];
        var url = "/admin/cliente/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteApellido(idCliente){
    var apellido = prompt("Ingrese el nuevo valor: ");
    if(apellido == "" || apellido == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'apellido'];
        var valoresParam = [idCliente, apellido];
        var url = "/admin/cliente/editarApellido";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteCedula(idCliente){
    var cedula = prompt("Ingrese el nuevo valor: ");
    if(cedula == "" || cedula == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'cedula'];
        var valoresParam = [idCliente, cedula];
        var url = "/admin/cliente/editarCedula";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteDpto(idCliente){
    var departamento = prompt("Ingrese el nuevo valor: ");
    if(departamento == "" || departamento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'departamento'];
        var valoresParam = [idCliente, departamento];
        var url = "/admin/cliente/editarDpto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteMunicipio(idCliente){
    var municipio = prompt("Ingrese el nuevo valor: ");
    if(municipio == "" || municipio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'municipio'];
        var valoresParam = [idCliente, municipio];
        var url = "/admin/cliente/editarMunicipio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteDireccion(idCliente){
    var direccion = prompt("Ingrese el nuevo valor: ");
    if(direccion == "" || direccion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'direccion'];
        var valoresParam = [idCliente, direccion];
        var url = "/admin/cliente/editarDireccion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteTelefono(idCliente){
    var telefono = prompt("Ingrese el nuevo valor: ");
    if(telefono == "" || telefono == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'telefono'];
        var valoresParam = [idCliente, telefono];
        var url = "/admin/cliente/editarTel";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteCorreo(idCliente){
    var correo = prompt("Ingrese el nuevo valor: ");
    if(correo == "" || correo == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'correo'];
        var valoresParam = [idCliente, correo];
        var url = "/admin/cliente/editarCorreo";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteNacimiento(idCliente){
    var fecha_nacimiento = prompt("Ingrese el nuevo valor: ");
    if(fecha_nacimiento == "" || fecha_nacimiento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'fecha_nacimiento'];
        var valoresParam = [idCliente, fecha_nacimiento];
        var url = "/admin/cliente/editarNac";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteContrasena(idCliente){
    var contrasena = prompt("Ingrese el nuevo valor: ");
    if(contrasena == "" || contrasena == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'contrasena'];
        var valoresParam = [idCliente, contrasena];
        var url = "/admin/cliente/editarContra";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarClienteFoto(idCliente){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idCliente', 'url_foto'];
        var valoresParam = [idCliente, url_foto];
        var url = "/admin/cliente/editarImagen";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}


/*
###################################################################################################################
###########################################Comentario - Allison####################################################
###################################################################################################################
*/

function editarComentarioContenido(idComentario){
    var comentario = prompt("Ingrese el nuevo valor: ");
    if(comentario == "" || comentario == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idComentario', 'comentario'];
        var valoresParam = [idComentario, comentario];
        var url = "/admin/comentario/editarContenido";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarComentarioValoracion(idComentario){
    var valoracion = prompt("Ingrese el nuevo valor: ");
    if(valoracion == "" || valoracion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idComentario', 'valoracion'];
        var valoresParam = [idComentario, valoracion];
        var url = "/admin/comentario/editarValoracion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarComentarioFechaHora(idComentario){
    var fechahora = prompt("Ingrese el nuevo valor: ");
    if(fechahora == "" || fechahora == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idComentario', 'fechahora'];
        var valoresParam = [idComentario, fechahora];
        var url = "/admin/comentario/editarFechaHora";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

/*
###################################################################################################################
########################################### Emprendedor - Mónica ###############################################
###################################################################################################################
*/

function editarEmprendedorNombre(idEmprendedor){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'nombre'];
        var valoresParam = [idEmprendedor, nombre];
        var url = "/admin/emprendedor/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorApellido(idEmprendedor){
    var apellido = prompt("Ingrese el nuevo valor: ");
    if(apellido == "" || apellido == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'apellido'];
        var valoresParam = [idEmprendedor, apellido];
        var url = "/admin/emprendedor/editarApellido";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorCedula(idEmprendedor){
    var cedula = prompt("Ingrese el nuevo valor: ");
    if(cedula == "" || cedula == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'cedula'];
        var valoresParam = [idEmprendedor, cedula];
        var url = "/admin/emprendedor/editarCedula";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorDepartamento(idEmprendedor){
    var departamento = prompt("Ingrese el nuevo valor: ");
    if(departamento == "" || departamento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'departamento'];
        var valoresParam = [idEmprendedor, departamento];
        var url = "/admin/emprendedor/editarDepartamento";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorMunicipio(idEmprendedor){
    var municipio = prompt("Ingrese el nuevo valor: ");
    if(municipio == "" || municipio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'municipio'];
        var valoresParam = [idEmprendedor, municipio];
        var url = "/admin/emprendedor/editarMunicipio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorDireccion(idEmprendedor){
    var direccion = prompt("Ingrese el nuevo valor: ");
    if(direccion == "" || direccion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'direccion'];
        var valoresParam = [idEmprendedor, direccion];
        var url = "/admin/emprendedor/editarDireccion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorTelefono(idEmprendedor){
    var telefono = prompt("Ingrese el nuevo valor: ");
    if(telefono == "" || telefono == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'telefono'];
        var valoresParam = [idEmprendedor, telefono];
        var url = "/admin/emprendedor/editarTelefono";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorCorreo(idEmprendedor){
    var correo = prompt("Ingrese el nuevo valor: ");
    if(correo == "" || correo == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'correo'];
        var valoresParam = [idEmprendedor, correo];
        var url = "/admin/emprendedor/editarCorreo";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorFechaNac(idEmprendedor){
    var fecha_nacimiento = prompt("Ingrese el nuevo valor: ");
    if(fecha_nacimiento == "" || fecha_nacimiento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'fecha_nacimiento'];
        var valoresParam = [idEmprendedor, fecha_nacimiento];
        var url = "/admin/emprendedor/editarFechaNac";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorContrasena(idEmprendedor){
    var contrasena = prompt("Ingrese el nuevo valor: ");
    if(contrasena == "" || contrasena == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'contrasena'];
        var valoresParam = [idEmprendedor, contrasena];
        var url = "/admin/emprendedor/editarContrasena";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendedorURL_Foto(idEmprendedor){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendedor', 'url_foto'];
        var valoresParam = [idEmprendedor, url_foto];
        var url = "/admin/emprendedor/editarUrlFoto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
/*
###################################################################################################################
####################################### Emprendimiento - Allison####################################################
###################################################################################################################
*/

function editarEmprendimientoNombre(idEmprendimiento){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'nombre'];
        var valoresParam = [idEmprendimiento, nombre];
        var url = "/admin/emprendimiento/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoDepartamento(idEmprendimiento){
    var departamento = prompt("Ingrese el nuevo valor: ");
    if(departamento == "" || departamento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'departamento'];
        var valoresParam = [idEmprendimiento, departamento];
        var url = "/admin/emprendimiento/editarDepartamento";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoMunicipio(idEmprendimiento){
    var municipio = prompt("Ingrese el nuevo valor: ");
    if(municipio == "" || municipio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'municipio'];
        var valoresParam = [idEmprendimiento, municipio];
        var url = "/admin/emprendimiento/editarMunicipio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoDireccion(idEmprendimiento){
    var direccion = prompt("Ingrese el nuevo valor: ");
    if(direccion == "" || direccion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'direccion'];
        var valoresParam = [idEmprendimiento, direccion];
        var url = "/admin/emprendimiento/editarDireccion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoDescripcion(idEmprendimiento){
    var descripcion = prompt("Ingrese el nuevo valor: ");
    if(descripcion == "" || descripcion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'descripcion'];
        var valoresParam = [idEmprendimiento, descripcion];
        var url = "/admin/emprendimiento/editarDescripcion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoURL_Foto(idEmprendimiento){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'url_foto'];
        var valoresParam = [idEmprendimiento, url_foto];
        var url = "/admin/emprendimiento/editarUrlFoto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoLinkFacebook(idEmprendimiento){
    var link_facebook = prompt("Ingrese el nuevo valor: ");
    if(link_facebook == "" || link_facebook == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'link_facebook'];
        var valoresParam = [idEmprendimiento, link_facebook];
        var url = "/admin/emprendimiento/editarLinkFacebook";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoLinkYoutube(idEmprendimiento){
    var link_youtube = prompt("Ingrese el nuevo valor: ");
    if(link_youtube == "" || link_youtube == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'link_youtube'];
        var valoresParam = [idEmprendimiento, link_youtube];
        var url = "/admin/emprendimiento/editarLinkYoutube";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoLinkInstagram(idEmprendimiento){
    var link_instagram = prompt("Ingrese el nuevo valor: ");
    if(link_instagram == "" || link_instagram == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'link_instagram'];
        var valoresParam = [idEmprendimiento, link_instagram];
        var url = "/admin/emprendimiento/editarLinkInstagram";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarEmprendimientoLinkTwitter(idEmprendimiento){
    var link_twitter = prompt("Ingrese el nuevo valor: ");
    if(link_twitter == "" || link_twitter == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idEmprendimiento', 'link_twitter'];
        var valoresParam = [idEmprendimiento, link_twitter];
        var url = "/admin/emprendimiento/editarLinkTwitter";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
/*
###################################################################################################################
#################################################### Feria - Mónica ###############################################
###################################################################################################################
*/

function editarFeriaNombre(idFeria){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'nombre'];
        var valoresParam = [idFeria, nombre];
        var url = "/admin/feria/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaDescripcion(idFeria){
    var descripcion = prompt("Ingrese el nuevo valor: ");
    if(descripcion == "" || descripcion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'descripcion'];
        var valoresParam = [idFeria, descripcion];
        var url = "/admin/feria/editarDescripcion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaDepartamento(idFeria){
    var departamento = prompt("Ingrese el nuevo valor: ");
    if(departamento == "" || departamento == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'departamento'];
        var valoresParam = [idFeria, departamento];
        var url = "/admin/feria/editarDepartamento";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaMunicipio(idFeria){
    var municipio = prompt("Ingrese el nuevo valor: ");
    if(municipio == "" || municipio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'municipio'];
        var valoresParam = [idFeria, municipio];
        var url = "/admin/feria/editarMunicipio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaDireccion(idFeria){
    var direccion = prompt("Ingrese el nuevo valor: ");
    if(direccion == "" || direccion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'direccion'];
        var valoresParam = [idFeria, direccion];
        var url = "/admin/feria/editarDireccion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaFechaInicio(idFeria){
    var fecha_inicio = prompt("Ingrese el nuevo valor: ");
    if(fecha_inicio == "" || fecha_inicio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'fecha_inicio'];
        var valoresParam = [idFeria, fecha_inicio];
        var url = "/admin/feria/editarFechaInicio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaFechaFin(idFeria){
    var fecha_fin = prompt("Ingrese el nuevo valor: ");
    if(fecha_fin == "" || fecha_fin == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'fecha_fin'];
        var valoresParam = [idFeria, fecha_fin];
        var url = "/admin/feria/editarFechaFin";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarFeriaURL_Foto(idFeria){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idFeria', 'url_foto'];
        var valoresParam = [idFeria, url_foto];
        var url = "/admin/feria/editarUrlFoto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
/*
###################################################################################################################
############################################ Producto - Allison####################################################
###################################################################################################################
*/

function editarProductoNombre(idProducto){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idProducto', 'nombre'];
        var valoresParam = [idProducto, nombre];
        var url = "/admin/producto/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarProductoDescripcion(idProducto){
    var descripcion = prompt("Ingrese el nuevo valor: ");
    if(descripcion == "" || descripcion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idProducto', 'descripcion'];
        var valoresParam = [idProducto, descripcion];
        var url = "/admin/producto/editarDescripcion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarProductoPrecio(idProducto){
    var precio = prompt("Ingrese el nuevo valor: ");
    if(precio == "" || precio == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idProducto', 'precio'];
        var valoresParam = [idProducto, precio];
        var url = "/admin/producto/editarPrecio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarProductoUrlFoto(idProducto){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idProducto', 'url_foto'];
        var valoresParam = [idProducto, url_foto];
        var url = "/admin/producto/editarUrlFoto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarProductoDisponible(idProducto){
    var disponible = prompt("Ingrese el nuevo valor: ");
    if(disponible == "" || disponible == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idProducto', 'disponible'];
        var valoresParam = [idProducto, disponible];
        var url = "/admin/producto/editarDisponible";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

/*
###################################################################################################################
################################################# Servicio - Mónica ###############################################
###################################################################################################################
*/

function editarServicioNombre(idServicio){
    var nombre = prompt("Ingrese el nuevo valor: ");
    if(nombre == "" || nombre == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idServicio', 'nombre'];
        var valoresParam = [idServicio, nombre];
        var url = "/admin/servicio/editarNombre";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarServicioDescripcion(idServicio){
    var descripcion = prompt("Ingrese el nuevo valor: ");
    if(descripcion == "" || descripcion == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idServicio', 'descripcion'];
        var valoresParam = [idServicio, descripcion];
        var url = "/admin/servicio/editarDescripcion";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarServicioUrlFoto(idServicio){
    var url_foto = prompt("Ingrese el nuevo valor: ");
    if(url_foto == "" || url_foto == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idServicio', 'url_foto'];
        var valoresParam = [idServicio, url_foto];
        var url = "/admin/servicio/editarUrlFoto";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}

function editarServicioDisponible(idServicio){
    var disponible = prompt("Ingrese el nuevo valor: ");
    if(disponible == "" || disponible == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idServicio', 'disponible'];
        var valoresParam = [idServicio, disponible];
        var url = "/admin/servicio/editarDisponible";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}
function editarServicioPrecio(idServicio){
    var disponible = prompt("Ingrese el nuevo valor: ");
    if(disponible == "" || disponible == null){
        alert('Error al actualizar');
    }else{
        var nombreParam = ['idServicio', 'precio'];
        var valoresParam = [idServicio, disponible];
        var url = "/admin/servicio/editarPrecio";
        realizarPeticion(url, nombreParam, valoresParam,"Edición Exitosa!");
    }
}


function fechasxd(fechaV){
    console.log('EN EL FOCOOO')
    var fecha = document.getElementById('fecha_nacimiento');
    fecha.valueAsDate = new Date(fechaV.split('/').reverse().join('/'))
}
