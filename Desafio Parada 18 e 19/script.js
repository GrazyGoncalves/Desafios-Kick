function trocarCor() {
    var cor = prompt("Escolha a cor do fundo do site?");
    
    if (cor) {
      document.body.style.backgroundColor = cor;
    }
  }