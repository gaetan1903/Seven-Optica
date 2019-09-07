$(function(){
  eel.all_verres()(print_all_verre);
});


function ajout(){
  if ($('#ajout-form #atype option:selected').val() != ''){

      if ($('#ajout-form #atraitement option:selected').val() != ''){

          if ($('#degre-list option:selected').val() != ''){
              eel.ajouter_verre($('#ajout-form #atype option:selected').val(), $('#ajout-form #atraitement option:selected').val(), $('#ajout-form #degre-list option:selected').val(), $('#ajout-form #anombre').val(), $('#ajout-form #aachat').val(), $('#ajout-form #avente').val())(feed_ajout);
          }
          else{
            alert('Veuillez selectionner le degré');
          }
      }
      else{
          alert('Veuillez selectionner le traitement ');
      }
  }
  else{
    alert('Veuillez selectionner un Type de verre');
  }
}

function feed_ajout(response){
  if (response == true){
     alert('success');
     $('#myModal2').modal('hide');
     window.location.reload();
  }
  else {
    alert("erreur s'est produit");
    $('#myModal2').modal('hide');
    window.location.reload();
  }
}


function print_all_verre(verre){
  vr = $('tbody tr');
  for (i=0; i<verre.length; i++){
      vr_clone = vr.clone();
      vr_clone.attr('id', verre[i][0]);

      vr_clone.find('input').attr('value', verre[i][0]);
      vr_clone.find('label').attr('for', 'checkbox'+ verre[i][0]);

      vr_clone.find('#reference').html(verre[i][1]);
      vr_clone.find('#type').html(verre[i][2]);
      vr_clone.find('#traitement').html(verre[i][3]);
      vr_clone.find('#degre').html(verre[i][4]);
      vr_clone.find('#quantite').html(verre[i][5]);
      vr_clone.find('#disponible').html(verre[i][5] - verre[i][6]);
      vr_clone.find('#achat').html(verre[i][7]);
      vr_clone.find('#vente').html(verre[i][8]);

      vr_clone.find('.edit').attr('onclick', 'myModalf3('+verre[i][0]+')');
      vr_clone.find('.delete').attr('onclick', 'deleteEmployeeModalf('+verre[i][0]+')');
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
    eel.select_verre(val)(myModalValue);
}


function myModalValue(tab) {
  alert(tab[0]);
  $("#myModal3 form").attr('value', tab[0]);
  $("#myModal3 #ref-verre").append("<option selected='selected'>"+ tab[1] +"</option>");
  $("#myModal3 #atype").append("<option selected='selected'>"+ tab[2] +"</option>");
  $("#myModal3 #atraitement").append("<option selected='selected'>"+ tab[3] +"</option>");
  $("#myModal3 #degre-list").append("<option selected='selected'>"+ tab[4] +"</option>");
  $("#myModal3 #anombre").attr('value', tab[5]);
  $("#myModal3 #aachat").attr('value', tab[6]);
  $("#myModal3 #avente").attr('value', tab[7]);
  $("#myModal3").modal('show');
}

function modifie(){
  eel.modifier_verre('verre', $("#myModal3 form").attr('value'), $("#myModal3 #anombre").val(), $("#myModal3 #aachat").val(), $("#myModal3 #avente").val())(modifie_fb);
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

function delete_verre(){
  eel.delete('verre', $("#deleteEmployeeModal form").attr('value'))(success_delete);
}

function success_delete(rep){
  if (rep==true){
    $('#deleteEmployeeModal').modal('hide');
    window.location.reload();
    alert('Effacer avec succes');
  }
  else{
    $('#deleteEmployeeModal').modal('hide');
    alert("Une erreur s'est produite")


  }

}

function multi_delete(){
  checkbox = $('tbody input[type="checkbox"]');
  checkbox.each( function(){
    if (this.checked == true){
        eel.delete('verre', this.value);
    }
  });
  alert('Tous les champs ont été supprimé');
  window.location.reload();
}

function degre_change(){
  if ($('#ref-deg').val() == "Sphere"){
    $('#degre-list').html(' ');
    $('#degre-list').append("<option value=''>Choisir degré Sphere</option>");
    for (i=40; i>=0; i--){
       html = "<option>"+ parseFloat(-i/4).toFixed(2) + "</option>";
       $('#degre-list').append(html);
    }

    for (i=1; i<41; i++){
       html = "<option>+"+ parseFloat(i/4).toFixed(2) + "</option>";
       $('#degre-list').append(html);
    }
  }
  else if ($('#ref-deg').val() == "Cylindre") {
    $('#degre-list').html(' ');
    $('#degre-list').append("<option value=''>Choisir degré Cylindre</option>");
    for (i=40; i>=0; i--){
       html = "<option>("+  parseFloat(-i/4).toFixed(2) + ")</option>";
       $('#degre-list').append(html);
    }

    for (i=1; i<41; i++){
       html = "<option>(+"+ parseFloat(i/4).toFixed(2) + ")</option>";
       $('#degre-list').append(html);
    }

  }

  else if ($('#ref-deg').val() == "Torique") {
    $('#degre-list').html(' ');

    $('#degre-list').append("<option value=''>Choisir degré Torique</option>");
    for (j=-40;j<40;j++){
      if (j<1){
        for (i=-40;i<1;i++){
          html = "<option>"+ parseFloat(i/4).toFixed(2) + "(" +  parseFloat(j/4).toFixed(2)  +")</option>";
          $('#degre-list').append(html);
        }

        for (i=1;i<41;i++){
          html = "<option>+"+ parseFloat(i/4).toFixed(2) + "(" + parseFloat(j/4).toFixed(2) +  ")</option>";
          $('#degre-list').append(html);
        }
      }
      else{
        for (i=-40;i<1;i++){
          html = "<option>"+ parseFloat(i/4).toFixed(2) + "(+" +  parseFloat(j/4).toFixed(2) +")</option>";
          $('#degre-list').append(html);
        }

        for (i=1;i<41;i++){
          html = "<option>+"+ parseFloat(i/4).toFixed(2) + "(+" + parseFloat(j/4).toFixed(2) +  ")</option>";
          $('#degre-list').append(html);
        }
      }
    }

  }
  else {
    $('#degre-list').html(' ');
  }
}
