from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
import hashlib
import mysql.connector

user = ''

class Auth:
    def __init__(self):     
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.title('Authentification')
        self.root.config(bg='white')
        self.root.geometry('400x425+475+75')

        try:
            self.connexion = mysql.connector.connect(host="localhost",user="gaetan",password="gaetan", database="optica")
        except:
            self.root.withdraw()
            showerror('Erreur de serveur base de donnée', "Veuillez allumer le serveur de base de donnée local")
            exit()

        self.cursor = self.connexion.cursor(buffered=True)
        self.user = StringVar()
        self.user.set('gaetan1903')
        self.password = StringVar()
        self.password.set('gaetan1903')


    def outils(self):
        self.logo0 = PhotoImage(file='image\logo.png')
        self.logo = self.logo0.subsample(3, 3)

        self.font14 = Font(family='Arial', size=14)


    def __corps__(self):
        Label(self.root, image = self.logo).pack(pady=5)
        Label(self.root, bg ='white').pack(pady=3)
        Label(self.root, text = "Nom d'utilisateur", bg = 'white', font=self.font14, fg = 'teal').pack()
        Entry(self.root, textvariable=self.user, bg = 'lightgray', width = 20, font = self.font14).pack()
        Label(self.root, bg ='white').pack(pady=5)
        Label(self.root, text = "Mot de passe", font=self.font14, bg ='white',  fg = 'teal').pack()
        Entry(self.root, textvariable=self.password, bg = 'lightgray', show='*', width=20, font=self.font14).pack()
        self.notification = Label(self.root, text='', fg='red', bg='white')
        self.notification.pack()
        Button(self.root, text = 'Connexion', command = self.fconnexion, font=self.font14).pack(pady=10)

    
    def fconnexion(self):
        self.notification.config(text='')
        self.notification.update()

        self.cursor.execute("SELECT User FROM personnel WHERE User = %s;", (self.user.get(), ))

        if self.cursor.fetchone() is not None:
            self.cursor.execute("SELECT Password FROM personnel WHERE User = %s;", (self.user.get(), ))

            if self.cursor.fetchone()[0] == hashlib.sha1(self.password.get().encode()).hexdigest():
                self.root.quit()
                self.root.destroy()
                self.connexion.close()
                #  exec(open("./principal.py").read())  #  lance un autre fichier
                fenPrincipal(self.user.get())

            else:
                self.notification.config(text="Mot de passe incorrecte")
                self.notification.update()

        else:
            self.notification.config(text="Nom d'utilisateur incorrecte")
            self.notification.update()

        
    def __final__(self):
        self.root.mainloop()


class Fenetre:
    def __init__(self, user):
        self.user = user
        self.root = Tk()
        self.root.title('Seven Optica: Logiciel de Vente')
        self.root.geometry('1000x600+150+25')
        self.root.resizable(width=False, height=False)
        self.root.config(bg='white')
        self.connexion = mysql.connector.connect(host="localhost",user="gaetan",password="gaetan", database="optica")
        self.cursor = self.connexion.cursor()
        self.menuTop()


    def __outils__(self):
        self.helpIm0 = PhotoImage(file='image\help.png')
        self.homeIm0 = PhotoImage(file='image\home.png')
        self.infoUserIm0 = PhotoImage(file='image\infoUser.png')
        self.helpIm = self.helpIm0.subsample(10, 10)
        self.infoUserIm = self.infoUserIm0.subsample(10, 10)
        self.homeIm = self.homeIm0.subsample(10, 10)
        self.venteIm0 = PhotoImage(file='image\Vente.png')
        self.venteIm = self.venteIm0.subsample(4, 4)
        self.factureIm0 = PhotoImage(file='image\\facturation.png')
        self.factureIm = self.factureIm0.subsample(3, 3)
        self.historiqueIm0 = PhotoImage(file='image\historique.png')
        self.historiqueIm = self.historiqueIm0.subsample(4, 4)
        self.stockIm = PhotoImage(file='image\gestion.png')
        self.arial20 = Font(family='Arial', size=20, slant=ITALIC, weight=BOLD)
        self.arial24 = Font(family='Arial', size=24, slant=ITALIC, weight=BOLD)
        self.arial7 = Font(family='Arial', size=7, slant=ITALIC)
    

    def menuTop(self):
        """
            focntion permettant de realiser des menu en haut 
                                                            """
        self.menubutton = Menu(self.root) 
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)  
        self.sous_menubutton_2 = Menu(self.menubutton, tearoff = 0)
        self.sous_menubutton_3 = Menu(self.menubutton, tearoff = 0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.menubutton.add_cascade(label = "Edition"  , menu = self.sous_menubutton_2)
        self.menubutton.add_cascade(label = "Aide"  , menu = self.sous_menubutton_3)

        self.sous_menubutton_1.add_command(label ="Ouvrir un autre projet")
        self.sous_menubutton_1.add_command(label ="Menu Principal")
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.root.quit)
        '''
        self.sous_menubutton_2.add_command(label ="Afficher la Réponse", )
        self.sous_menubutton_2.add_command(label ="Changer nom d'equipe", command = lambda: self.changerEquiName(changed="nom d'equipe", name=True))
        self.sous_menubutton_2.add_command(label ="Changer nombre de joueur eliminé", command = lambda: self.changerEquiName(changed="nombre d'equipe(s) eliminé(s)", nbrEl=True))
        '''
        self.sous_menubutton_3.add_command(label ="Documentation")
        self.sous_menubutton_3.add_command(label ="Afficher la license")
        self.sous_menubutton_3.add_command(label ="A propos Developpeur")
        self.sous_menubutton_3.add_command(label ="A propos du logiciel")
        self.root.config(menu = self.menubutton)

        self.__outils__()
        self.__corps__()

    def whois(self, event):
        self.cursor.execute("select Nom, Prenom from personnel where User = %s", ((self.user, )))
        result = self.cursor.fetchone()
        nom = result[0]
        prenom = result[1]
        showinfo('Utilisateur Info', f' Utilisateur {self.user} : {nom} {prenom}')
    
    def __corps__(self):
        head = Canvas(self.root, width = 1000, height = 60, bg = 'teal')
        head.place(relx = -0.002 , rely = -0.001)
        head.create_text(500, 30, text= '☺ Seven Optica ☺', font = self.arial24, fill = 'yellow')
        # head.create_image(970, 31, image = self.helpIm)
        head.create_image(35, 31, image = self.homeIm)
        head_user = Canvas(self.root, width = 85, height = 60, bg='teal', highlightthickness = 0)
        head_user.place(relx=0.91, rely = 0.001)
        head_user.create_image(45, 30, image = self.infoUserIm)
        head_user.bind('<Button-1>', self.whois)
        #  ***************
        foot = Canvas(self.root, width = 1000, height = 25, bg = 'teal')
        foot.place(relx=-0.002, rely=0.97)
        foot.create_text(75, 10, text='powered by Gaetan Jonathan', font=self.arial7, fill='yellow')
        foot.create_text(950, 10, text='copyright Août 2019', font=self.arial7, fill='yellow')
        # head.create_text(450, 60, text= '☻ une meilleure vision ☺', font = self.arial18, fill = 'yellow')

        vente = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        vente.place(relx=0.20, rely=0.12)
        vente.create_image(150, 100, image = self.venteIm)
        vente.create_text(150, 200, text = 'Vente', font = self.arial20)
        facture = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        facture.place(relx=0.65, rely=0.12)
        facture.create_image(150, 100, image = self.factureIm)
        facture.create_text(150, 200, text = 'Facturation', font = self.arial20)
        historique = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        historique.place(relx=0.20, rely=0.55)
        historique.create_image(150, 100, image = self.historiqueIm)
        historique.create_text(150, 200, text = 'Historique', font = self.arial20)
        stock = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        stock.place(relx=0.65, rely=0.57)
        stock.create_image(150, 100, image = self.stockIm)
        stock.create_text(150, 200, text = 'Stock', font = self.arial20)
        self.cadre = Frame(self.root, width = 200, height = 520)
        self.cadre.place(relx=0, rely = 0.105)

        



    def __final__(self):
        self.root.mainloop()


def fenPrincipal(user):
    fen = Fenetre(user)
    fen.__final__()
    


if __name__ == '__main__':
    log = Auth()
    log.outils()
    log.__corps__()
    log.__final__()


        