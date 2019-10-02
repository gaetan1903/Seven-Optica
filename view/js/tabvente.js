monture_product = '';

$(function(){
  eel.all_prodcut()(recvProduct);  // appel d'une fonction python
});


function recvProduct(response){
  // fonction recevant le retour de la fonction python appeler
  monture_product = response;
  is_yet = new Array()
  for (i=0;i<response[0].length;i++){
    ref = response[0][i][1];
    if (is_yet.indexOf(ref) < 0){
      $('#vente_monture #reference').append('<option>' + response[0][i][1] + '</option>');
      is_yet.push(ref);
    }
    //$('#vente_monture #couleur').append('<option>' + response[0][i][2] + '</option>');
    //$('#vente_monture #forme').append('<option value='+ response[0][i][3] + '>');
  }
  $('#vente_monture #nombre').html('<option>0</option>'); // on  remplace directement

  for (i=0;i<response[1].length;i++){
    $('#vente_verre #type').append('<option>' + response[1][i][1] + '</option>');
    //$('#vente_verre #traitement').append('<option>' + response[1][i][2] + '</option>');
    //$('#vente_verre #degre').append('<option>' + response[1][i][3] + '</option>');
  }
  $('#vente_verre #nombre').html('<option>0</option>');  // on remplace directement

}


function refChange(obj){
  if (obj == 'reference'){
      var valRef = $("#vente_monture input[list='reference']").val();
      $('#vente_monture #forme').html('');
      $("#vente_monture input[list='forme']").val('');
      for (i=0;i<monture_product[0].length;i++){
        if (monture_product[0][i][1] == valRef ){
          $('#vente_monture #forme').append('<option value='+ monture_product[0][i][3] + '>');
        }
      }
  }
  else if (obj == 'forme'){
    var valRef = $("#vente_monture input[list='reference']").val();
    var valFor = $("#vente_monture input[list='forme']").val();
    $("#vente_monture input[list='couleur']").val('');
    for (i=0;i<monture_product[0].length;i++){
      if (monture_product[0][i][1] == valRef && monture_product[0][i][3] == valFor){
        $('#vente_monture #couleur').append('<option value='+ monture_product[0][i][2] + '>');

      }
    }
  }

  else if (obj == 'couleur'){
    var valRef = $("#vente_monture input[list='reference']").val();
    var valFor = $("#vente_monture input[list='forme']").val();
    var valCol = $("#vente_monture input[list='couleur']").val();
    $("#vente_monture input[list='nombre']").val('');
    for (i=0;i<monture_product[0].length;i++){
      if (monture_product[0][i][1] == valRef && monture_product[0][i][3] == valFor && monture_product[0][i][2] == valCol){
        $('#vente_monture #nombre').html('');
        for (j=1;j<=monture_product[0][i][4];j++){
          $('#vente_monture #nombre').append('<option value=' + j + '>');
        }

      }
    }

  }
}
