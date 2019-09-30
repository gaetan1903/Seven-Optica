$(function(){
  eel.all_prodcut()(recvProduct);  // appel d'une fonction python
});


function recvProduct(response){
  // fonction recevant le retour de la fonction python appeler

  for (i=0;i<response[0].length;i++){
    $('#vente_monture #reference').append('<option>' + response[0][i][1] + '</option>');
    $('#vente_monture #couleur').append('<option>' + response[0][i][2] + '</option>');
    //$('#vente_monture #forme').append('<option value='+ response[0][i][3] + '>');
  }
  $('#vente_monture #nombre').append('<option>1</option>');

  for (i=0;i<response[1].length;i++){
    $('#vente_verre #type').append('<option>' + response[1][i][1] + '</option>');
    $('#vente_verre #traitement').append('<option>' + response[1][i][2] + '</option>');
    $('#vente_verre #degre').append('<option>' + response[1][i][3] + '</option>');
  }
  $('#vente_verre #nombre').append('<option>1</option>');

}
