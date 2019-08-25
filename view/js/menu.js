usr = ''
function user_info(user){
    $('.name').html(user[0]);
    $('#date').html(user[1]);
}
$(function() {
    eel.info_usr()(user_info);
  });



function ouvrir(ino){
    alert(hey);
    eel.ouvrir(ino)();
}