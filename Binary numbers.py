import hashlib
import matplotlib.pyplot as plt

#unos parametara
unosAlgoritma = input("Unesite algoritam kriptiranja: ")

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

for broj in range(2**8):
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

#maxValue = max(lista)/int(brojPonavljanja)
#minValue = min(lista)/int(brojPonavljanja)

plt.figure(dpi=150)
plt.title(unosAlgoritma.capitalize())
plt.plot(lista, color='red', linewidth=0.5)
#plt.ylabel(str(minValue) + "-" + str(maxValue))
#plt.xlabel("Broj generiranih poruka: " + brojPonavljanja)
plt.show()