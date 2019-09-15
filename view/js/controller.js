var usr ='' ;
function authentification(){
        user = document.getElementById("user");
        password = document.getElementById("password");
        usr = user.value;
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
    window.location = 'menu.html';

};
