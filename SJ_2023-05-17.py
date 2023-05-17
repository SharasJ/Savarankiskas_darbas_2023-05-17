# #1 uzduotis

def gauti_pirmas_raides(vardai):
    pirmos_raides = [vardas[0] for vardas in vardai]
    return pirmos_raides

vardai = ['Jonas', 'Antanas', 'Marytė', 'Jurgis', 'Giedrius', 'Tomas', 'Lukas']
rezultatas = gauti_pirmas_raides(vardai)

print(rezultatas)

# antra uzduotis

def pašalinti_dublikatus(skaiciu_sarasas):
    unikalūs_elementai = tuple(set(skaiciu_sarasas))
    return unikalūs_elementai

skaiciu_sarasas = (1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 3, 3, 2, 2, 1)
unikalus_sarasas = pašalinti_dublikatus(skaiciu_sarasas)
print(unikalus_sarasas)

#3 uzduotis

import pickle


def sukurti_darbuotoja(vardas, amzius, darbo_pozicija):
    darbuotojas = {
        "vardas": vardas,
        "amzius": amzius,
        "darbo_pozicija": darbo_pozicija
    }
    return darbuotojas


def issaugoti_darbuotojus(darbuotojai, failo_pavadinimas):
    with open(failo_pavadinimas, "wb") as failas:
        pickle.dump(darbuotojai, failas)


def uzkrauti_darbuotojus(failo_pavadinimas):
    with open(failo_pavadinimas, "rb") as failas:
        darbuotojai = pickle.load(failas)
    return darbuotojai


darbuotojai = [
    sukurti_darbuotoja("Jonas", 24, "pagalbinis darbuotojas"),
    sukurti_darbuotoja("Marius", 28, "vairuotojas"),
    sukurti_darbuotoja("Zigmas", 58, "komikas"),
    sukurti_darbuotoja("Loreta", 37, "vyr. buhaltere"),
    sukurti_darbuotoja("Petras", 22, "asistentas"),
    sukurti_darbuotoja("Jolanta", 33, "valytoja"),
    sukurti_darbuotoja("Linas", 42, "direktorius"),
    sukurti_darbuotoja("Zita", 47, "skyriaus vadove")
]


issaugoti_darbuotojus(darbuotojai, "darbuotojai.pkl")


uzkrauti_duomenys = uzkrauti_darbuotojus("darbuotojai.pkl")
print(uzkrauti_duomenys)


amzius_suma = sum(darbuotojas["amzius"] for darbuotojas in uzkrauti_duomenys)
vidurkis = amzius_suma / len(uzkrauti_duomenys)


with open("trecios_uzduoties_duomenys.txt", "w") as rezultatu_failas:
    rezultatu_failas.write("Vidurkis: " + str(vidurkis))

# ketvirta uzduotis:

def skaiciu_vidurkiai(sarasas):
    rezultatas = []
    for elementas in sarasas:
        tekstas, skaiciu_sarasas = elementas
        vidurkis = sum(skaiciu_sarasas) / len(skaiciu_sarasas)
        rezultatas.append((tekstas, vidurkis))
    return rezultatas


duomenys = [("obuolys", [1, 2, 3]), ("bananas", [4, 5, 6]), ("apelsinas", [7, 8, 9])]


rezultatas = skaiciu_vidurkiai(duomenys)
print(rezultatas)

# penkta uzduotis:

from functools import reduce

def skaiciu_vidurkis(skaiciu_sarasas):
    suma = reduce(lambda x, y: x + y, skaiciu_sarasas)
    vidurkis = suma / len(skaiciu_sarasas)
    return vidurkis

with open("skaiciai.txt", "r") as failas:
    skaiciai = failas.read().split(",")
    skaiciai = [int(s.strip()) for s in skaiciai]
print(skaiciai)

vidurkis = skaiciu_vidurkis(skaiciai)

with open('rezultatas.txt', 'w') as failas:
    failas.write(str(vidurkis))

print("Vidurkis:", vidurkis)
