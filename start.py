#-*-coding : utf8 -*-
import eel, mysql.connector, hashlib, webbrowser
from datetime import datetime

eel.init('view')

usr, liaison = '', ''
moisFr = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet' ,'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

def model():
    try:
        global liaison
        liaison = mysql.connector.connect(host="localhost",user="gaetan",password="gaetan", database="optica")
    except:
        return "Erreur de connexion avec la base de donnee, Peut etre qu'il est eteint, \n Essayer de l'allume d'abord "
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
        global usr
        usr = user
        return 'ok'
    else:
        return validation

@eel.expose
def info_usr():
    liaison = model()
    cursor = liaison.cursor(buffered=True)
    cursor.execute(" SELECT * FROM personnel WHERE User = %s", ((usr, )))
    info = cursor.fetchone()
    jour = datetime.today().day
    mois = datetime.today().month
    annee = datetime.today().year
    mois = moisFr[mois - 1]
    return [usr, f"{jour} {mois} {annee}", info[1], info[2]]


@eel.expose
def verify_admin(username):
    liaison = model()
    cursor = liaison.cursor(buffered=True)
    cursor.execute(" SELECT admin FROM personnel WHERE User =%s", ((username, )))
    admin = cursor.fetchone()
    return admin[0]


@eel.expose
def ouvrir(rse):
    if rse == 'facebook':
        webbrowser.open('https://facebook.com/gaetan1903', autoraise=True)
    elif rse == 'github':
        webbrowser.open('https://github.com/gaetan1903', autoraise=True)
    elif rse == 'linkedin':
        webbrowser.open('https://linkedin.com/in/gaetanj', autoraise=True)


@eel.expose
def ajouter_verre(types, traitement, degre, nombre, achat, vente):
    liaison = model()
    cursor = liaison.cursor()
    ref = 'V' + types[0].upper() + traitement[0].upper()
    if degre[0] != '(' and degre[-1] != ')':
        ref = ref + 'c' + str(degre).replace('-', 'm').replace('+', 'p')

    elif degre[0] != '(' and degre[-1] ==')' :
        dg = degre.split('(')
        dg[0] = dg[0].replace('-', 'm').replace('+', 'p')
        dg[1] = dg[1][:-1].replace('-', 'm').replace('+', 'p')
        print(dg)
        ref = ref + 't' + '-'.join(dg)

    elif degre[0] == '(' and degre[-1] == ')':
        ref = ref + 's' + degre[1:-1].replace('-', 'm').replace('+', 'p')

    try:
        cursor.execute("""
            INSERT INTO verre(Ref, Type_Verre, Traiter, Degre, Nombre_Stock, Prix_Achat,  Prix_Vente)
             values(%s, %s, %s, %s, %s, %s, %s);
        """, ((ref, types, traitement, degre, nombre, achat, vente)) )
        liaison.commit()
    except:
        return False
    else:
        return True


@eel.expose
def all_verres():
    liaison = model()
    cursor = liaison.cursor()

    cursor.execute("""
        SELECT * FROM verre;
    """)
    verre = cursor.fetchall()
    return verre



eel.start('home.html', size=(1000, 600), position=(175, 75))
