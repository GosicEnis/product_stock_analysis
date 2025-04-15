# Kreiranje rjecnika sa podacima o prodaji
sales = {
    "Laptop": 15,
    "Mouse": 150,
    "Keyboards": 85,
    "Monitor": 30,
    "USB cables": 200,
}

# a) Izracunavanje ukupne kolicine prodatih proizvoda
ukupno_prodatih = 0
for quantity in sales.values():
    ukupno_prodatih += quantity

# b) Pronalazenje najprodavanijeg proizvoda
najprodavaniji_proizvod = ""
najprodavanija_kolicina = 0

for product in sales:
    if sales[product] > najprodavanija_kolicina:
        najprodavanija_kolicina = sales[product]
        najprodavaniji_proizvod = product

# c) Pronalazenje najmanje prodavanog proizvoda
najmanje_prodavan_proizvod = ""
najmanja_kolicina = float("inf")

for product in sales:
    if sales[product] < najmanja_kolicina:
        najmanja_kolicina = sales[product]
        najmanje_prodavan_proizvod = product

# d) Provera da li je "Web camera" prodavana i dodavanje ako nije
if "Web camera" not in sales:
    sales["Web camera"] = 0

# e) Ispravka greske, povecavanje broja prodatih monitora za 5
sales["Monitor"] = sales["Monitor"] + 5

# Ispis azuriranog rjecnika
print("Azurirani podaci o prodaji:", sales)

# Ispis informacija
print(f"Ukupna kolicina prodatih proizvoda: {ukupno_prodatih} jedinica")
print(f"Najprodavaniji proizvod: {najprodavaniji_proizvod} ({najprodavanija_kolicina} jedinica)")
print(f"Najmanje prodavan proizvod: {najmanje_prodavan_proizvod} ({najmanja_kolicina} jedinica)")
print(f"Da li je 'Web camera' dodana? {'Da' if sales['Web camera'] == 0 else 'Ne'}")


# Funkcija za pronalazenje kriticnih proizvoda (manje od 50 prodatih jedinica)
def kriticni_proizvodi(sales):
    kriticni = []
    for product in sales:
        if sales[product] < 50:
            kriticni.append(product)
    return kriticni


# Ispis liste kriticnih proizvoda
kriticni = kriticni_proizvodi(sales)
if kriticni:
    print("Proizvodi sa kriticnom prodajom:", kriticni)
else:
    print("Nema proizvoda sa kriticnom prodajom.")

# Provera validnosti podataka (da li postoji negativna prodaja)
negativni_proizvodi = []
for product in sales:
    if sales[product] < 0:
        negativni_proizvodi.append(product)

if negativni_proizvodi:
    print("Greska! Pronadjeni su proizvodi sa negativnom prodajom:", negativni_proizvodi)
else:
    print("Svi podaci su validni - nema negativnih vrednosti.")