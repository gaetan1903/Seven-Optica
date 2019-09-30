monture_product = '';

$(function(){
  eel.all_prodcut()(recvProduct);  // appel d'une fonction python
});


function recvProduct(response){
  // fonction recevant le retour de la fonction python appeler
  monture_product = response;
  is_yet = new Array();
  for (i=0;i<response[0].length;i++){
    $('#vente_monture #reference').append('<option>' + response[0][i][1] + '</option>');
    //$('#vente_monture #couleur').append('<option>' + response[0][i][2] + '</option>');
    //$('#vente_monture #forme').append('<option value='+ response[0][i][3] + '>');
  }
  $('#vente_monture #nombre').html('<option>0</option>'); // on  remplace directement

  for (i=0;i<response[1].length;i++){
    if !(response[1][i][1] in is_yet){
      $('#vente_verre #type').append('<option>' + response[1][i][1] + '</option>');
      is_yet.push(response[1][i][1])
    }

    //$('#vente_verre #traitement').append('<option>' + response[1][i][2] + '</option>');
    //$('#vente_verre #degre').append('<option>' + response[1][i][3] + '</option>');
  }
  $('#vente_verre #nombre').html('<option>0</option>');  // on remplace directement

}


function refChange(obj){
  if (obj == 'monture'){
      var val = ($("#vente_monture input[list='reference']").val());

      for (i=0;i<monture_product[0].length;i++){
        if (response[0][i][1] == val ){
          $('#vente_monture #forme').append('<option value='+ response[0][i][3] + '>');
      }
      }
  }

}
