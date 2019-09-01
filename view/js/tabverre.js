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
      vr_clone.find('#disponible').html(verre[i][5] - verre[i][6]);
      vr_clone.find('#achat').html(verre[i][7]);
      vr_clone.find('#vente').html(verre[i][8]);

      vr_clone.find('#myModal3').attr('id', 'mod'+ verre[i][0]);
      vr_clone.find('#deleteEmployeeModal').attr('id', 'del'+ verre[i][0]);
      vr_clone.appendTo('tbody');
  }
  vr.remove();

  var checkbox = $('tbody input[type="checkbox"]');
  $("#selectAll").click(function(){
            if(this.checked){
                      checkbox.each(function(){
                                this.checked = true;
                      });
            } else{
                      checkbox.each(function(){
                                this.checked = false;
                      });
            }
  });
  checkbox.click(function(){
            if(!this.checked){
                      $("#selectAll").prop("checked", false);
            }
  });
}



function myModal3(val){
  $("#myModal3").attr('value', val);
  $("#myModal3").modal('show');
}
