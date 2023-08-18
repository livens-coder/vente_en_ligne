from .products import pwodwi_list

lis_acha = []

def panye_acha():
    global lis_acha
    print("Kisa ou vle achte:")
    for index, pwodwi in enumerate(pwodwi_list, start=1):
        print(f"{index}. Non: {pwodwi['name']},    Pri: gdes {pwodwi['price']},    Kantite: {pwodwi['quantity']}")
    
    try:
        while True:
            chwa = input("Antre nimewo pwodwi ou vle a ou peze '0' pou fini: ")
            
            if chwa == '0':
                break
            
            index_chwa = int(chwa) - 1
            if 0 <= index_chwa < len(pwodwi_list):
                pwodwi_chwa = pwodwi_list[index_chwa]
                nom_pwodwi = pwodwi_chwa['name']
                pri_pwodwi = pwodwi_chwa['price']
                kantite_max = pwodwi_chwa['quantity']
                
                kantite_achete = int(input(f"Kantite {nom_pwodwi} ou vle achte (max {kantite_max}): "))
                
                if 0 <= kantite_achete <= kantite_max:
                    pwodwi_chwa['quantity'] -= kantite_achete
                    lis_acha.append({"name": nom_pwodwi, "price": pri_pwodwi, "quantity": kantite_achete})
                    print(f"Ou ajoute nan panye ou: {nom_pwodwi} - Pri: gdes {pri_pwodwi}, Kantite: {kantite_achete}")
                else:
                    print("Kantite a pa valide.")
            else:
                print("Pwodwi a pa valide.")
    except EOFError:
        print("W fini ak achte pwodwi yo.")

    print("Panye a gen pwodwi yo:")
    for pwodwi_achete in lis_acha:
        print(f"{pwodwi_achete['name']} - Pri: gdes {pwodwi_achete['price']}, Kantite: {pwodwi_achete['quantity']}")

def kalkile_prix_total():
    total = sum(pwodwi['price'] * pwodwi['quantity'] for pwodwi in lis_acha)
    return total

panye_acha()
prix_total = kalkile_prix_total()
print(f"Prix total nan panye a se: gdes {prix_total}")
