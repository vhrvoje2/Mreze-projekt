import random
import hashlib
import string
import matplotlib.pyplot as plt

#generiranje random stringa
def randomString(stringLen):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for i in range(stringLen))

#generiranje sazetka
def hashFunkcija(string, algoritam):
    sazetak = hashlib.new(algoritam, string.encode())
    return sazetak.hexdigest()

#unos parametara
stringLen = int(input("Unesite duljinu poruke: "))
unosAlgoritma = input("Unesite algoritam kriptiranja: ")
brojPonavljanja = input("Unesite broj poruka koje zelite generirati: ")

#md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(), sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.
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

#lista za brojanje
lista = []
for x in range(velicinaListe):
    lista.append(0)

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

maxValue = max(lista)/int(brojPonavljanja)
minValue = min(lista)/int(brojPonavljanja)

if brojPonavljanja == "1":
    print("Generiran string: ")
    print(generiranString)
    print()

    print("Generiran sazetak: ")
    print(generiranHash)
    print()

    print("Generiran sazetak u binarnom obliku: ")
    print(binarniHash)
    print(len(binarniHash))

if int(brojPonavljanja) > 1:
    plt.figure(dpi=150)
    plt.title(unosAlgoritma.capitalize())
    plt.plot(lista, color='red', linewidth=0.5)
    plt.ylabel(str(minValue) + "-" + str(maxValue))
    plt.xlabel("Broj generiranih poruka: " + brojPonavljanja)
    plt.show()