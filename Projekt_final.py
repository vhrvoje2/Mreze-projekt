import random
import hashlib
import string
import matplotlib.pyplot as plt

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()

window.title("Analiza ravnomjernosti kriptografskih sažetaka")
window.geometry('500x250')

# TITLE label
lbl_title = Label(window, text="Generiranje kriptografskog sažetka", font=("Arial Bold", 14))
lbl_title.grid(column=0, row=0, sticky=W)

# Label: Duljina poruke
lbl_strlen = Label(window, text="Unesite duljinu poruke:", font=("Arial", 12))
lbl_strlen.grid(column=0, row=1, sticky=W)

# Lenght input
lenght_input = Entry(window,width=20)
lenght_input.grid(column=1, row=1, sticky=W)

# Label: Broj poruka
lbl_br_por = Label(window, text="Unesite broj poruka koje zelite generirati: ", font=("Arial", 12))
lbl_br_por.grid(column=0, row=2, sticky=W)

# Number input
num_input = Entry(window,width=20)
num_input.grid(column=1, row=2, sticky=W)

# Label: Algoritam kriptiranja
lbl_algoritam = Label(window, text="Odaberite algoritam kriptiranja: ", font=("Arial", 12))
lbl_algoritam.grid(column=0, row=3, sticky=W)

# Combobox
combo = Combobox(window, state='readonly')
combo['values']= ('md5','sha1','sha224','sha256','sha384','sha512','blake2b','blake2s','sha3_224','sha3_256','sha3_384','sha3_512')
combo.current(0) #set the selected item
# Get value -> combo.get()
combo.grid(column=1, row=3, sticky=W)

#generiranje random stringa
def randomString(stringLen):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for i in range(stringLen))

#generiranje sazetka
def hashFunkcija(string, algoritam):
    sazetak = hashlib.new(algoritam, string.encode())
    return sazetak.hexdigest()

#postavljanje veličine liste za brojanje
#md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(), sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.
def velListe(unosAlgoritma):
    if unosAlgoritma == "md5":
        velicinaListe = 128
    elif unosAlgoritma == "sha1":
        velicinaListe = 160
    elif unosAlgoritma in ("sha224", "sha3_224"):
        velicinaListe = 224
    elif unosAlgoritma in ("sha256", "blake2s", "sha3_256"):
        velicinaListe = 256
    elif unosAlgoritma in ("sha384", "sha3_384"):
        velicinaListe = 384
    elif unosAlgoritma in ("sha512", "sha3_512", "blake2b"):
        velicinaListe = 512
    return velicinaListe

def praznaLista(velicinaListe):
    lista = []
    for x in range(velicinaListe):
        lista.append(0)
    return lista

# Button
def clicked():
    #unos parametara
    stringLen = int(lenght_input.get())
    unosAlgoritma = combo.get()
    brojPonavljanja = num_input.get()
    velicinaListe = velListe(unosAlgoritma)
    lista = praznaLista(velicinaListe)
    
    for x in range(int(brojPonavljanja)):
        #generiranje stringa
        generiranString = randomString(stringLen)

        #generiranje hasha
        generiranHash = hashFunkcija(generiranString, unosAlgoritma)

        #pretvaranje u binarni oblik
        binarniHash = (bin(int(generiranHash, 16)))[2:]
        binarniHash = binarniHash.zfill(velicinaListe)
        
        #brojacki loop
        for y in range(len(binarniHash)):
            if binarniHash[y] == "1":
                lista[y] += 1

    maxValue = round(max(lista)/int(brojPonavljanja), 4)
    minValue = round(min(lista)/int(brojPonavljanja), 4)

    if brojPonavljanja == "1":
        ispis = "GENERIRANI STRING: \n"+generiranString+"\n\nGENERIRANI SAZETAK: \n"+generiranHash+"\n\nGENERIRANI SAZETAK U BINARNOM OBLIKU: \n"+binarniHash
        messagebox.showinfo("Ispis", ispis)

    if int(brojPonavljanja) > 1:
        plt.figure(dpi=150)
        plt.title(unosAlgoritma.capitalize())
        plt.axis([-5, len(lista)+5, 0, int(brojPonavljanja)])
        plt.plot(lista, color='red', linewidth=0.5)
        plt.ylabel(str(minValue) + "-" + str(maxValue))
        plt.xlabel("Broj generiranih poruka: " + brojPonavljanja)
        plt.show()
    
btn = Button(window, text="Generiraj graf", command=clicked)
btn.grid(column=1, row=4, sticky=W)

# TITLE #2 label
lbl_title_B = Label(window, text="Binarni brojevi", font=("Arial Bold", 14))
lbl_title_B.grid(column=0, row=6, sticky=W)

# Label: Broj potencije
lbl_br_por = Label(window, text="Unesite potenciju broja 2: ", font=("Arial", 12))
lbl_br_por.grid(column=0, row=7, sticky=W)

# Number input binary
num_input_B = Entry(window,width=20)
num_input_B.grid(column=1, row=7, sticky=W)

# Label: Algoritam kriptiranja
lbl_algoritam_B = Label(window, text="Odaberite algoritam kriptiranja: ", font=("Arial", 12))
lbl_algoritam_B.grid(column=0, row=8, sticky=W)

# Combobox
combo_B = Combobox(window, state='readonly')
combo_B['values']= ('md5','sha1','sha224','sha256','sha384','sha512','blake2b','blake2s','sha3_224','sha3_256','sha3_384','sha3_512')
combo_B.current(0) #set the selected item
# Get value -> combo.get()
combo_B.grid(column=1, row=8, sticky=W)

# Button Binary
def clicked_B():
    unosPotencije = int(num_input_B.get())
    unosAlgoritma = combo_B.get()
    #lista za brojanje
    lista = []
    velicinaListe = velListe(unosAlgoritma)

    for x in range(velicinaListe):
        lista.append(0)

    for broj in range(2**unosPotencije):
        #pretvaranje u binarni oblik
        binBroj = bin(int(broj))[2:]

        #generiranje hasha
        generiranHash = hashlib.new(unosAlgoritma, binBroj.encode()).hexdigest()

        binarniHash = bin(int(generiranHash, 16))[2:]
        binarniHash = binarniHash.zfill(velicinaListe)
        
        #brojacki loop
        for y in range(velicinaListe-len(binarniHash), len(binarniHash)):
            if binarniHash[y] == "1":
                lista[y] += 1

    maxValue = round(max(lista)/2**unosPotencije, 4)
    minValue = round(min(lista)/2**unosPotencije, 4)

    plt.figure(dpi=150)
    plt.title(unosAlgoritma.capitalize())
    plt.axis([-5, len(lista)+5, 0, int(2**unosPotencije)])
    plt.plot(lista, color='red', linewidth=0.5)
    plt.ylabel(str(minValue) + "-" + str(maxValue))
    plt.xlabel("Broj generiranih brojeva: " + str(2**unosPotencije))
    plt.show()

btn_b = Button(window, text="Generiraj graf", command=clicked_B)
btn_b.grid(column=1, row=9, sticky=W)

window.mainloop()