function ajout(){
  alert('allo');
  eel.ajouter_verre(document.getElementById('atype').value, document.getElementById('atraitement').value, document.getElementById('adegre').value, document.getElementById('anombre').value , document.getElementById('aachat').value, document.getElementById('avente').value )(feed_ajout);
  alert('allo again');

}


function feed_ajout(response){
  console.log(response);
}
