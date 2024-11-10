# Následující text převeďte na množinu unikátních znaků, zjistěte počet unikátních znaků a vypište jejich seřazený seznam.

# text = '''Prágl
# Prágl, po anglánsku Prague nebo Praha nebo v Cajsku, je taková lochna
# v tem kuse hródy někde za čárama naši domoviny, kde se zoncna už
# nechláme a kde se prndá po cajzlovsku. A ještě k temu tam majó sicnu
# těžcí papaláši, kvůli čemu ho má každé v láfu jako kaktus ve véfuku.
# Z Práglu bere kramále aj ten jejich len kerému se péruje Vltava.

# O Práglu se taky kóří, pač tam majó hafo retychů pro všecky. Kromě
# bůry švédských retychů só aj dva v Olmecu a jeden v Bučovicách.
# To my z našeho štatlu radši hážem lulec do kašny na Zelňáku. Když
# ale nekdo vopruboval zašrajbčit náš barocké Parnas do cancu retychů
# pro všecky, přišmrdolili se ti Švédi s tým, že só proti a hókajó po
# celé hródě, že ta vasra v tem se dá chlemtat.
# '''

# unikatni_znaky = set(text)

# pocet_unikatnich_znaku = len(unikatni_znaky)
# seznam_unikatnich_znaku = sorted(unikatni_znaky)

# print(pocet_unikatnich_znaku)
# print(seznam_unikatnich_znaku)

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().

# vysvedceni = {'český jazyk': 2, 'matematika': 1, 'dějepis': 1}
# print(vysvedceni)

# Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# Zkopíruj si slovník do svého programu.
# Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
# U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

# sales['Noc, která mě zabila'] = 0
# sales['Vrah zavolá v deset'] += 100

# print(sales)

# V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
# Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
# Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.

# cislo = input('Zadejte číslo svého lístku: ')
# if not cislo.isdigit():
#     print(f'Vámi zadaný znak {cislo} neodpovídá žádanému formátu. ')
#     exit()
# else:
#     cislo = int(cislo)
    
# if cislo not in tombola:
#     print('Bohužel nevyhráváš nic')
# else:
#     print(f'Hurá, vyhráváš {tombola[cislo]}. ')


# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. 
# Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, 
# zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

# jmeno = input('Zadej své jméno. ')

# if jmeno not in passwords:
#     print('Tvé jméno není na seznamu. ')
#     exit()
# else:
#     heslo = input('Zadej své heslo: ')
#     if passwords[jmeno] == heslo:
#         print('Smíš vstoupit.')
#     else:
#         print('Neznáš heslo, běž pryč!')
        
    
# Uvažujme vysvědčení, které máme zapsané jako slovník.

# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

# import statistics

# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }

# marks_list = []
# mark_1_subject = []

# for predmet, znamka in school_report.items():
#     marks_list.append(znamka)
#     if znamka == 1:
#         mark_1_subject.append(predmet)

# average_mark = statistics.mean(marks_list)
# print(average_mark)
# print(mark_1_subject)

# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]

# total_pages = 0
# good_rating_books = 0

# for line in books:
#     total_pages += line['pages']
#     if line['rating'] >= 8:
#         good_rating_books += 1
    
# print(total_pages)
# print(good_rating_books)

# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. 
# Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

# plates = {"4A2 3000": "František Novák",
#     "6P5 4747": "Jana Pilná",
#     "3B7 3652": "Jaroslav Sečkár",
#     "1P5 5269": "Marta Nováková",
#     "37E 1252": "Martina Matušková",
#     "2A5 2241": "Jan Král"}

# pilsen_owners = []

# for plate, owner in plates.items():
#     if plate[1] == 'P':
#         pilsen_owners.append(owner)
        
# print(pilsen_owners)

# Pohlédněte na následující reprezentaci receptu:

# import math

# recept = {
#     'nazev': 'Batáty se šalvějí a pancettou',
#     'narocnost': 'stredni',
#     'doba': 30,
#     'ingredience': [
#         ['batát', '1', '15 kč'],
#         ['olivový olej', '2 lžíce', '2 kč'],
#         ['pancetta', '4-6 plátků', '21 kč'],
#         ['přepuštěné máslo', '2 lžíce', '5 kč'],
#         ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
#         ['sůl', '1/2 lžičky', '0.1 kč'],
#         ['muškátový oříšek', 'špetka', '1 kč'],
#         ['česnek', '2 stroužky', '1 kč'],
#         ['šalvějové lístky', '20-25', '12 kč']
#     ]
# }
# Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
# Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.

# cena_jidla = 0

# for polozka in recept['ingredience']:
#     cena = float(polozka[2][:-3])
#     cena_jidla += cena
    
# cena_jidla = math.ceil(cena_jidla)
# print(cena_jidla)


purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]

# Zkus dotáhnout náš program na finanční vypořádání spolubydlících. Z lekce si můžeš zkopírovat kódy, 
# které vytvoří slovník s útratami jednotlivých spolubydlících a výpočet průměrné útraty na osobu. 
# Dopiš cyklus, který projde slovník sum_per_person a pro každého ze spolubydlících vypíše, 
# kolik by měl doplatit (pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).

sum_per_person = {}
for item in purchase_list:
    person = item["Jméno"]
    value = item["Částka"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value
        
           
total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")
    
average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

for person, value in sum_per_person.items():
    difference = value - average_value 
    if difference == 0:
        print(f'{person} zaplatil za společné nákupy {value} Kč, nemá nedoplatek ani přeplatek.')
    elif difference < 0:
        print(f'{person} má nedoplatek {abs(round(difference))} Kč.')
    else:
        print(f'{person} má přeplatek {round(difference)} Kč.')