import eel, mysql.connector, hashlib

eel.init('view')


def model():
    try:
        liaison = mysql.connector.connect(host="localhost",user="gaetan",password="gaetan", database="optica")
    except:
        return "Erreur de connexion avec la base de donnée, Peut être qu'il est éteint, \n Essayer de l'allumé d'abord "
    else:
        return liaison 


def authentification(user, password):
    try:
        liaison = model()
    except:
        pass
    else:
        cursor = liaison.cursor(buffered=True)
        cursor.execute("""
                SELECT User FROM personnel WHERE User = %s;
        """, (user, ))

        if cursor.fetchone() is not None:
            cursor.execute("""
            SELECT Password FROM personnel WHERE User = %s;
            """, (user, ))

            if cursor.fetchone()[0] == hashlib.sha1(password.encode()).hexdigest():
                return True

            else:
                return "Mot de passe Incorrect"

        else:
            return "Nom d'utilisateur Incorrect"

    
@eel.expose
def auth(user, password):
    validation = authentification(user, password)
    if validation == True:
        return 'ok'
    else:
        return validation


eel.start('index0.html', size=(1000, 600), position=(175, 75), mode=None)