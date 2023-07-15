const buttonHeader = document.getElementById('button-header')
const navbarNav = document.getElementById('navbarNav')

function mostrarOcultar(){
  navbarNav.classList.toggle('show')
}

buttonHeader.addEventListener('click', mostrarOcultar)