from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
import hashlib
import mysql.connector

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
        self.password = StringVar()


    def outils(self):
        self.logo = PhotoImage(file='image\logo.png')
        self.logo = self.logo.subsample(3, 3)
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
                import principal 

            else:
                self.notification.config(text="Mot de passe incorrecte")
                self.notification.update()

        else:
            self.notification.config(text="Nom d'utilisateur incorrecte")
            self.notification.update()

        
    def __final__(self):
        self.root.mainloop()



if __name__ == '__main__':
    log = Auth()
    log.outils()
    log.__corps__()
    log.__final__()


        