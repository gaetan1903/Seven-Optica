$(function(){
eel.all_verres()(print_all_verre);
});

function print_all_verre(verre){
  vr = $('tbody tr');
  for (i=0; i<verre.length; i++){
      vr_clone = vr.clone();
      vr_clone.attr('id', verre[i][0]);

      vr_clone.find('input').attr({id: 'checkbox' + verre[i][0], value: "'" + verre[i][0]} + "'");
      vr_clone.find('label').attr('for', 'checkbox'+ verre[i][0]);

      vr_clone.find('#reference').html(verre[i][1]);
      vr_clone.find('#type').html(verre[i][2]);
      vr_clone.find('#traitement').html(verre[i][3]);
      vr_clone.find('#degre').html(verre[i][4]);
      vr_clone.find('#quantite').html(verre[i][5]);
      vr_clone.find('#disponible').html(verre[i][6]);
      vr_clone.find('#achat').html(verre[i][7]);
      vr_clone.find('#vente').html(verre[i][8]);


      /*
      $('tbody #'+ verre[i][0] + ' input').attr(id:'checkbox'+verre[i][0], value: verre[i][0]);
      $('tbody #'+ verre[i][0] + ' label').attr('for', 'checkbox'+ verre[i][0]);
      $('tbody #'+ verre[i][0] + ' td #reference').html(verre[i][1]);
    }
    */
    vr_clone.appendTo('tbody');
  }
  vr.remove();
}
