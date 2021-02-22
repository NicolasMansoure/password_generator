from tkinter import *
from random import randint, choice
import string
import tkinter
from tkinter.filedialog import asksaveasfile
import tkinter as tk
from tkinter import messagebox
#____________________________________________

password = ""

# fonction generateur de mot de passe.
def generate_password():
    password_min =12
    password_max = 19
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# fonction de validation pour quitter le logiciel.
def ExitApp():
    MsgBox = tk.messagebox.askquestion ("Quittez l'application","Voulez vous vraiement quittez l'apllication ?",icon = 'error')
    if MsgBox == 'yes':
       window.destroy()


#fonction pour enregisrer sous.
def enregistrer_sous():
    a = password_entry.get()
    file = asksaveasfile(title="Enregistrer sous …", defaultextension=".txt",filetypes=[('Text file','*.txt'),("HTML file","*.html"),("All files",".*")])
    file.write(a)


# cree une fenetre.
window = Tk()
window.title("Générateur de mot de passe.")
window.geometry("720x480")
window.minsize(500,300)
window.iconbitmap("lock.ico")
window.config(background="#ABE3D5")

# cree la frame principale.
frame = Frame(window, bg="#ABE3D5")

# cree une image.
width = 170
height = 170
image = PhotoImage (file="lock.png")
canvas = Canvas(frame, width=width, height=height, bg="#ABE3D5", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0,column=0,sticky=W)

# cree une sous boite.
right_frame = Frame (frame, bg="#ABE3D5")

# cree un titre.
label_title = Label(right_frame, text="Mot de passe", font=("bebas neue",30), bg="#ABE3D5", fg="white", pady=10)
label_title.pack()

# cree un input.
password_entry = Entry(right_frame,text="0 0 0 0 0 ", font=("lato",20), bg="#ABE3D5", fg="white")
password_entry.pack(pady=20,padx=20)

# cree un bouton.
generate_password_button = Button(right_frame, text="Générer", font=("bebas neue",20), bg="#ABE3D5", fg="white", command=generate_password)
generate_password_button.pack(fill=X,padx=15)

# on place la sous boite a droite de la frame principale.
right_frame.grid(row=0,column=1,sticky=W)

# afficher la frame.
frame.pack(expand=YES)

# creation d'une barre de menu.
menu_bar = Menu(window)
# cree un premier menu.
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau mot de passe", command=generate_password)
file_menu.add_command(label="Enregistrer sous …", command= enregistrer_sous)
file_menu.add_command(label='Quitter', command=ExitApp)
password = generate_password()
# configurer la fenetre pour ajouter le menu bar.
window.config(menu=menu_bar)


# afficher la fenete.
window.mainloop()