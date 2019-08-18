
function authentification(){
        user = document.getElementById("user");
        password = document.getElementById("password");

        eel.auth(user.value, password.value)(print_return);
}

function print_return(reponse){
    if (reponse == 'ok'){
        home();
    }
    else{
           show(reponse);  
    }
}   

function show(reponse){
    $('#erreur').html(reponse);
    $('#Modal').modal('show');
}

function home(){
    window.location = 'acceuil.html';
    
};

$(function() {
    $('#nom_home').html('Hello world. Ce texte est affiché par jQuery.');
  });