from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
import hashlib, mysql.connector, random, time
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
        self.index_monture = ('Code', 'Reference', 'Couleur', 'Forme', 'Prix de Vente', "Prix d'achat", 'Quantité', 'Reservé', 'Disponible')
        self.index_verre = ('Code', 'Type', 'Traitement', 'Degré', 'Prix de Vente', "Prix d'achat", 'Quantité', 'Reservé', 'Disponible')
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
        self.backIm0 = PhotoImage(file='image\\back.png')
        self.backIm = self.backIm0.subsample(8, 8)
        self.addIm0 = PhotoImage(file='image\\shop.png')
        self.addIm = self.addIm0.subsample(2, 2)
        self.arial20 = Font(family='Arial', size=20, slant=ITALIC, weight=BOLD)
        self.arial12 = Font(family='Arial', size=12, slant=ITALIC)
        self.arial24 = Font(family='Arial', size=24, slant=ITALIC, weight=BOLD)
        self.arial7 = Font(family='Arial', size=7, slant=ITALIC)
        self.font_grid = Font(family='Arial', weight='bold', size='12')
    

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
        head_home = Canvas(self.root, width = 85, height = 60, bg='teal', highlightthickness = 0)
        head_home.bind('<Button-1>', self.home)
        head_home.place(relx=0.01, rely=0.001)
        head_home.create_image(20, 31, image = self.homeIm)
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
        vente.bind('<Button-1>', self.vente)
        vente.place(relx=0.20, rely=0.12)
        vente.create_image(150, 100, image = self.venteIm)
        vente.create_text(150, 200, text = 'Vente', font = self.arial20)
        facture = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        facture.place(relx=0.65, rely=0.12)
        facture.create_image(150, 100, image = self.factureIm)
        facture.create_text(150, 200, text = 'Facturation', font = self.arial20)
        facture.bind('<Button-1>', self.facture)
        historique = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        historique.place(relx=0.20, rely=0.55)
        historique.create_image(150, 100, image = self.historiqueIm)
        historique.create_text(150, 200, text = 'Historique', font = self.arial20)
        historique.bind('<Button-1>', self.historique)
        stock = Canvas(self.root, width = 300 , height = 225, bg ='white', highlightthickness = 0, cursor='hand2', relief ='raised')
        stock.bind('<Button-1>', self.stock)
        stock.place(relx=0.65, rely=0.57)
        stock.create_image(150, 100, image = self.stockIm)
        stock.create_text(150, 200, text = 'Stock', font = self.arial20)
        self.cadre = Frame(self.root, width = 200, height = 520)
        self.cadre.place(relx=0, rely = 0.105)


    def fen_close(self,  fen):
        fen.destroy()
        self.root.deiconify()
        

    def home(self, event):
        self.root.quit()
        self.root.destroy()
        log = Auth()
        log.outils()
        log.__corps__()
        log.__final__()
        

    def vente(self, event):
        self.root.withdraw()
        self.fenVente = Toplevel(self.root)
        self.fenVente.title('Vente')
        self.fenVente.geometry('700x450+300+150')
        self.fenVente.protocol("WM_DELETE_WINDOW", lambda : self.fen_close(self.fenVente))
        head = Canvas(self.fenVente, width = 800, height = 35, bg = 'teal')
        head.place(relx = -0.003 , rely = -0.003)
        head_back = Canvas(self.fenVente, width = 75, height = 35, bg='teal', highlightthickness = 0)
        head_back.place(relx=0.001, rely = 0.003)
        head_back.create_image(15, 17, image = self.backIm)
        head_back.bind('<Button-1>', lambda f: self.backHome(self.fenVente))

    
    def facture(self, event):
        self.root.withdraw()
        self.fenFacture = Toplevel(self.root)
        self.fenFacture.title('Facturation')
        self.fenFacture.geometry('700x450+300+150')
        self.fenFacture.protocol("WM_DELETE_WINDOW", lambda : self.fen_close(self.fenFacture))
        head = Canvas(self.fenFacture, width = 800, height = 35, bg = 'teal')
        head.place(relx = -0.003 , rely = -0.003)
        head_back = Canvas(self.fenFacture, width = 75, height = 35, bg='teal', highlightthickness = 0)
        head_back.place(relx=0.001, rely = 0.003)
        head_back.create_image(15, 17, image = self.backIm)
        head_back.bind('<Button-1>', lambda f: self.backHome(self.fenFacture))

    
    def historique(self, event):
        self.root.withdraw()
        self.fenHistorique = Toplevel(self.root)
        self.fenHistorique.title('Historique')
        self.fenHistorique.geometry('700x450+300+150')
        self.fenHistorique.protocol("WM_DELETE_WINDOW", lambda : self.fen_close(self.historique))
        head = Canvas(self.fenHistorique, width = 800, height = 35, bg = 'teal')
        head.place(relx = -0.003 , rely = -0.003)
        head_back = Canvas(self.fenHistorique, width = 75, height = 35, bg='teal', highlightthickness = 0)
        head_back.place(relx=0.001, rely = 0.003)
        head_back.create_image(15, 17, image = self.backIm)
        head_back.bind('<Button-1>', lambda f: self.backHome(self.fenHistorique))
        

    def stock(self, event):
        colors = ('teal', '#D00B21', 'purple')
        color = colors[random.randint(0,2)]
        self.root.withdraw()
        self.fenStock = Toplevel(self.root)
        self.fenStock.title('Stock')
        self.fenStock.geometry('1200x650+75+25')
        self.fenStock.protocol("WM_DELETE_WINDOW", lambda : self.fen_close(self.fenStock))
        head = Canvas(self.fenStock, width = 1210, height = 35, bg = color, highlightthickness = 0)
        head.place(relx = -0.003 , rely = -0.003)
        head.create_text(600, 17, text = '♦ Gerer le Stock ♦', fill= 'yellow', font=Font(family='Arial', size = 12))
        head.create_image(1190, 17, image = self.addIm)
        head_back = Canvas(self.fenStock, width = 75, height = 30, bg = color, highlightthickness = 0)
        head_back.place(relx=0.005, rely = 0.003)
        head_back.create_image(15, 15, image = self.backIm)
        head_back.bind('<Button-1>', lambda f: self.backHome(self.fenStock))

        newStock = Button(self.fenStock, text ='Nouveau Stock', width= 15, relief = RAISED, cursor='hand2', fg= 'white', bg = color, font = Font(family='Arial', size = 20, slant='italic'), command = self.nouveauStock)
        newStock.place(relx=0.10, rely=0.15)
        statStock = Button(self.fenStock, text ='Statistique Stock', width= 15, relief = RAISED, cursor='hand2', fg= 'white', bg = color, font = Font(family='Arial', size = 20, slant='italic'))
        statStock.place(relx=0.375, rely=0.20)
        reduireStock = Button(self.fenStock, text ='Reduire Stock', width= 15, relief = RAISED, cursor='hand2', fg= 'white', bg = color, font = Font(family='Arial', size = 20, slant='italic'))
        reduireStock.place(relx=0.65, rely=0.15)

        self.montureBut = Canvas(self.fenStock, width=200, height=50, bg=color, relief ='flat', border = 2, cursor ='hand1', highlightthickness=2)
        self.montureBut.create_text(100, 27, text='MONTURE', font=Font(family='Arial', size = 14, weight='bold'), fill='white')
        self.montureBut.place(relx=0.2, rely=0.4)
        self.montureBut.bind('<Button-1>', lambda f: self.montureStock(color))

        self.verreBut = Canvas(self.fenStock, width=200, height=50, bg=color, relief ='flat', border = 2, cursor='hand1')
        self.verreBut.create_text(100, 27, text='VERRE', font=Font(family='Arial', size = 14, weight='bold'), fill='white')
        self.verreBut.place(relx=0.6, rely=0.4)
        self.verreBut.bind('<Button-1>', lambda f: self.verreStock(color))

        self.FrameStock = Frame(self.fenStock, width=1180, height = 253)
        self.FrameStock.place(relx=0.001, rely=0.57)
        self.FrameStock.grid_propagate(0)

        self.cursor.execute('select * from monture where quantite <> 0;')
        data = self.cursor.fetchall()
        self.stringGrid(self.index_monture, color, data)
        

    def nouveauStock(self):
        self.fenStock.withdraw()
        self.fenStockAdd = Toplevel(self.root)
        self.fenStockAdd.config(bg='white')
        self.fenStockAdd.title('SEVEN OPTICA: Nouveau Produit')
        self.fenStockAdd.geometry('600x400+200+100')


    def montureStock(self, color):
        self.montureBut.config(cursor='wait')
        self.cursor.execute('select * from monture where quantite <> 0;')
        data = self.cursor.fetchall()
        self.canvas.destroy()
        self.stringGrid(self.index_monture, color, data)
        self.montureBut.config(cursor='hand1')


    def verreStock(self, color):
        x = time.time()
        self.verreBut.config(cursor='wait')
        print('changement de curseur en: ', time.time() - x, ' seconde')
        self.cursor.execute('select * from verre where quantite <> 0;')
        print('finission base de donnée: ', time.time() - x, ' seconde')
        data = self.cursor.fetchall()
        print('extraction de base de donnée: ', time.time() - x, ' seconde')
        self.canvas.destroy()
        self.stringGrid(self.index_verre, color, data)
        print('fin de chargement: ', time.time() - x, ' seconde')
        self.verreBut.config(cursor='hand1')


    def stringGrid(self, index, color, data):
        self.canvas = Canvas(self.FrameStock, width=1180, height = 255)
        scroll_y = Scrollbar(self.FrameStock, orient="vertical", command=self.canvas.yview)
        tab = Frame(self.canvas)
        
        self.numberLines = len(data) + 1
        self.numberColumns = 9
        for i in range(self.numberLines):  
            for j in range(self.numberColumns):
                if i < 1:
                    if j == 3:
                        cell = Entry(tab, width=18, font=self.font_grid, bg=color, fg='white', bd=2)
                        cell.insert(0, index[j])
                    elif j > 5: 
                        cell = Entry(tab, width=9, font=self.font_grid, bg=color, fg='white', bd=2)
                        cell.insert(0, index[j])
                    else:
                        cell = Entry(tab, width=16, font=self.font_grid, bg=color, fg='white', bd=2)
                        cell.insert(0, index[j])
                else:
                    if j==3:
                        cell = Entry(tab, width=18, font=self.arial12)
                        cell.insert(0, data[i-1][j])
                    elif j==4 or j==5:
                        cell = Entry(tab, width=16, font=self.arial12)
                        cell.insert(0, f"Ar {data[i-1][j]}")
                    elif j>5:
                        cell = Entry(tab, width=9, font=self.arial12)
                        cell.insert(0, data[i-1][j])
                    else:
                        cell = Entry(tab, width=16, font=self.arial12)
                        cell.insert(0, data[i-1][j])
                
                cell.grid(row = i, column = j)

        self.canvas.create_window(0, 0, anchor='nw', window=tab)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=scroll_y.set)
                 
        self.canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right', padx=0)

        footer = Canvas(self.fenStock, width=1200, height=20, highlightthickness=0, bg=color)
        footer.place(relx=0, rely=0.97)


    def backHome(self, who):
        who.destroy()
        self.root.deiconify()


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


        