function valida(){
    let sobrenome = document.getElementById('sobrenome').value;

if(sobrenome == ""){
    alert("tem que preencher o sobrenome");
    document.getElementById('sobrenome').focus();
    return false;
}

const diaInput = document.getElementById('dia');
const mesInput = document.getElementById('mes');
const anoInput = document.getElementById('ano');


function preencherDataDeNascimento(dia, mes, ano) {
  diaInput.value = dia;
  mesInput.value = mes;
  anoInput.value = ano;
}

preencherDataDeNascimento(10, 5, 1990);

var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(email.value.match (mailformat)){
    return true
}else{
    alert('email esta invalido')
    email.focus()
    return false
}

if(senha.value.length < 6){
    alert('senha deve ser maior ou igual a 6')
    return false
}
return true
}