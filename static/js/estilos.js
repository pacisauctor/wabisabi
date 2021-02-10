function mostrarFormCliente(){
    formCliente = document.getElementById("formCliente");
    formEmprendedor = document.getElementById("formEmprendedor");
    formEmprendedor.style.display = "none";
    formCliente.style.display = "flex";
}
function mostrarFormEmprendedor(){
    formCliente = document.getElementById("formCliente");
    formEmprendedor = document.getElementById("formEmprendedor");
    formCliente.style.display = "none";
    formEmprendedor.style.display = "flex";
}