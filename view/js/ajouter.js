function ajout(){
  eel.ajouter_verre(document.getElementById('type').value, document.getElementById('traitement').value, document.getElementById('degre').value, document.getElementById('nombre').value , document.getElementById('achat').value , document.getElementById('vente').value )(feed_ajout);
  
}


function feed_ajout(response){
  console.log(response);
}
