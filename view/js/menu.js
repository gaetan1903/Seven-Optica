usr = ''
function user_info(user){
    $('.username').html(user[0]);
    $('#date').html(user[1]);
    $('.name').html(user[2])
    $('.prenom').html(user[3])
}
$(function() {
    eel.info_usr()(user_info);
  });


