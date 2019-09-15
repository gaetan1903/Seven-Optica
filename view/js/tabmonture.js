$(function(){
  eel.all_montures()(print_all_monture);
});


function ajout(){

      if ($('#ajout-form #color').val() != ''){

          if ($('#ajout-form #forme option:selected').val() != ''){
              eel.ajouter_monture($('#ajout-form #ref').val(), $('#ajout-form #color option:selected').val(), $('#ajout-form #forme option:selected').val(), $('#ajout-form #anombre').val(), $('#ajout-form #aachat').val(), $('#ajout-form #avente').val())(feed_ajout);
          }
          else{
            alert('Veuillez selectionner la forme');
          }
      }
      else{
          alert('Veuillez selectionner la couleur ');
      }
  }

function feed_ajout(msg){
  if (msg == true){
    alert('Ajouter avec Success');
  }
  else {
    alert(msg);
  }
}



function print_all_monture(monture){
  vr = $('tbody tr');
  for (i=0; i<monture.length; i++){
      vr_clone = vr.clone();
      vr_clone.attr('id', monture[i][0]);

      vr_clone.find('input').attr('value', monture[i][0]);
      vr_clone.find('label').attr('for', 'checkbox'+ monture[i][0]);

      vr_clone.find('#reference').html(monture[i][1]);
      vr_clone.find('#couleur').html(monture[i][2]);
      vr_clone.find('#forme').html(monture[i][3]);
      vr_clone.find('#quantite').html(monture[i][4]);
      vr_clone.find('#disponible').html(monture[i][4] - monture[i][5]);
      vr_clone.find('#achat').html(monture[i][6]);
      vr_clone.find('#vente').html(monture[i][7]);

      vr_clone.find('.edit').attr('onclick', 'myModalf3('+monture[i][0]+')');
      vr_clone.find('.delete').attr('onclick', 'deleteEmployeeModalf('+monture[i][0]+')');
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

function myModalf3(val){
    eel.select_monture(val)(myModalValue);
}

function myModalValue(tab) {
  $("#myModal3 form").attr('value', tab[0]);
  $("#myModal3 #ref").attr('value', tab[1])
  $("#myModal3 #color").append("<option selected='selected'>"+ tab[2] +"</option>");
  $("#myModal3 #forme").append("<option selected='selected'>"+ tab[3] +"</option>");
  $("#myModal3 #anombre").attr('value', tab[4]);
  $("#myModal3 #aachat").attr('value', tab[6]);
  $("#myModal3 #avente").attr('value', tab[7]);
  $("#myModal3").modal('show');
}

function modifie(){
  eel.modifier('monture', $("#myModal3 form").attr('value'), $("#myModal3 #anombre").val(), $("#myModal3 #aachat").val(), $("#myModal3 #avente").val())(modifie_fb);
}

function modifie_fb(response){
      if (response == true){
          alert('Modification effectuer');
      }
      else{
        alert("Une erreur s'est produite, Verifier votre saisie");
      }
}


function deleteEmployeeModalf(val){
  $("#deleteEmployeeModal form").attr('value', val);
  $("#deleteEmployeeModal").modal('show');
}

function delete_monture(){
  eel.delete('monture', $("#deleteEmployeeModal form").attr('value'))(success_delete);
}

function success_delete(rep){
  if (rep==true){
    $('#deleteEmployeeModal').modal('hide');
    window.location.reload();
    alert('Effacer avec succes');
  }
  else{
    $('#deleteEmployeeModal').modal('hide');
    alert("Une erreur s'est produite");
  }

}

function multi_delete(){
  checkbox = $('tbody input[type="checkbox"]');
  checkbox.each( function(){
    if (this.checked == true){
        eel.delete('monture', this.value);
    }
  });
  alert('Tous les champs selectionnés ont été supprimé');
  window.location.reload();
}
