# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. 
# Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc 
# za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. 
# Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. 
# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

# with open('vykaz.txt', mode='r', encoding='utf-8') as file:
#     vykaz = []
#     for line in file:
#         line = line.strip()
#         vykaz.append(int(line))

# print(vykaz)

# hodinova_mzda = input('Zadejte hodinovou mzdu v Kč: ')
# if not hodinova_mzda.isdigit():
#     print(f'Vámi zadaná mzda {hodinova_mzda} neodpovídá žádánému formátu. ')
# else:
#     hodinova_mzda = int(hodinova_mzda)
    
# vyplata_za_rok = sum(vykaz) * hodinova_mzda
# prumerna_vyplata_za_mesic = round(vyplata_za_rok / len(vykaz))
# print(vyplata_za_rok)
# print(prumerna_vyplata_za_mesic)

# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě. 
# Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. 
# Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
# Vypište na výstup počty slov na každém řádku
# Vypište na výstup celkový počet všech slov v souboru

# with open('praha.txt', mode='r', encoding='utf-8') as input_file:
#     pocet_slov_celkem = 0
    
#     for line in input_file:
#         words = line.strip().split()  # Použití split() bez argumentu
#         pocet_slov = len(words)
#         print(pocet_slov)
#         pocet_slov_celkem += pocet_slov

# print(f"Celkový počet slov v textu: {pocet_slov_celkem}")

# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, 
# kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů 
# za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali 
# a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

# with open('auta.txt', mode='r', encoding='utf-8') as input_file:
#     auta = []
#     for line in input_file:
#         line = line.replace(',', '.')
#         line = line.strip().split()
        
#         if len(line) == 2:
#             try:
#                 auta.append([line[0], float(line[1])])
#             except ValueError:
#                 print(f"Chyba při zpracování řádku: {line}")

# celkem_km = sum(km for _, km in auta)

# print(f"Celkový počet ujetých kilometrů: {celkem_km} tisíc km")


# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

# pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.

# with open('kalendar.txt', mode='w', encoding='utf-8') as output_file:
#     for mesic in pocty_dni:
#         print(mesic, file=output_file)
        
        
# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), 
# a pak se zeptá na řádek textu, který má do souboru zapsat.

# with open(input('Zadejte název souboru: '), mode='w', encoding='utf-8') as output_file:
#     print(input('Zadejte text: '), file=output_file)
    


# Rozepsaná výplata
# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na terminál
# Poté program upravte tak, aby vypsal tyto výsledky do souboru

# with open('vykaz.txt', mode='r', encoding='utf-8') as input_file:
#     vykaz = []
#     for line in input_file:
#         line = line.strip()
#         vykaz.append(line)

# hodinova_mzda = input('Zadejte Vaši hodinovou mzdu: ')
# if not hodinova_mzda.isdigit():
#     print(f'Zadaná mzda {hodinova_mzda} neodpovídá žádanému formátu. ')
# else:
#     hodinova_mzda = int(hodinova_mzda)
 
# hodiny_mzda = []           

# for hodiny in vykaz:
#     hodiny = int(hodiny)
#     vyplata = hodiny * hodinova_mzda
#     hodiny_mzda.append([hodiny, vyplata])
#     print(f'{hodiny} - {vyplata}')

# with open('vykaz_mzda.txt', mode='w', encoding='utf-8') as output_file:
#     for hodiny, vyplata in hodiny_mzda:
#         line = f'{hodiny} - {vyplata}'
#         print(line, file=output_file)
        
        
# Univerzita pro celoživotní vzdělávání se rozhodla změnit svůj známkovací systém z číselných známek 1 až 5 na hodnocení písmeny A až F. 
# Bohužel změna se odehrála jaksi uprostřed semestru, takže je potřeba změnit aktuální výkazy o známkách z čísel na písmena. Nechte se vést následujícím postupem.

# Otevřete si dokument s jedním výkazem známek.
# Zkopírujte si tuto tabulku do textového souboru.
# Napište program, který tuto tabulku načte ze souboru a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
# Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.
# Vytvořte novou Google tabulku, která vypadá stejně jako ta výše avšak s převedenými známkami.



# with open('znamky.tsv', mode='r', encoding='utf-8') as input_file:
#     znamky = []
#     for line in input_file:
#         line = line.strip().split('\t')
#         znamky.append(line)
        
# zmena_znamek = {
#     '1': 'A',
#     '2': 'B',
#     '3': 'C',
#     '4': 'D',
#     '5': 'F',
# }
# nove_znamky = []

# for student in znamky:
#     opraveny_student = []
#     for polozka in student:
#         if polozka in zmena_znamek:
#             opraveny_student.append(zmena_znamek[polozka])
#         else:
#             opraveny_student.append(polozka)
#     nove_znamky.append(opraveny_student)
    
# with open('nove_znamky.tsv', mode='w', encoding='utf-8') as output_file:
#     for line in nove_znamky:
#         line = '\t'.join(line)
#         print(line, file=output_file)
        
        
# Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu. Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět. 
# Data jsou uložená v souboru pasazeri.txt. Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.

# Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
# Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.

# with open('pasazeri.txt', mode='r', encoding='utf-8') as input_file:
#     jizdy_celkem = []
#     for radek in input_file:
#         radek = radek.strip()
#         jizdy_denne = radek.split()
#         trasa = []
        
#         for jizda in jizdy_denne:
#             jizda_split = jizda.split(',')
#             pasazeri_tam = int(jizda_split[0])
#             pasazeri_zpet = int(jizda_split[1])
#             trasa.append((pasazeri_tam, pasazeri_zpet))
#         jizdy_celkem.append(trasa)
            
# tam_prvni_den = 0
# zpet_prvni_den = 0

# for jizda in jizdy_celkem[0]:
#     tam_prvni_den += jizda[0]
#     zpet_prvni_den += jizda[1]
    
# tam_celkem = 0
# zpet_celkem = 0

# for trasa in jizdy_celkem:
#     for jizda in trasa:
#         tam_celkem += jizda[0]
#         zpet_celkem += jizda[1]
        
    
# print(tam_prvni_den)
# print(zpet_prvni_den)
# print(tam_celkem)
# print(zpet_celkem)
    
       

# Napište program, který vylosuje náhodnou hrací kartu z klasické whistové sady obsahující 52 karet, rozdělených do čtyř barev (kříže, srdce, piky, káry), 
# s hodnotami 2, 3, 4, 5, 6, 7, 8, 9, 10, J (kluk), Q (dáma), K (král), A (eso).

# Výstup programu může vypadat například takto:

# Karta: kluk kříže
import random

karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'kluk', 'dáma', 'král', 'eso']
barvy = ['kříže', 'srdce', 'piky', 'káry']

# vybrana_karta = random.choice(karty)
# vybrana_barva = random.choice(barvy)

# print(f'Karta: {vybrana_karta} {vybrana_barva}')

# Napište program, který vylosuje seznam 4 náhodných hracích karet podobně jako v předchozím úkolu. Můžeme si představovat, že rozdáváme karty například v pokeru. 
# Zatím pro jednoduchost nebudeme řešit, že se nám může nějaká karta v seznamu opakovat.

# Vymyslete, jak budete vylosovanou kartu v seznamu reprezentovat. Vypište pak tento seznam na výstup.
# Dále k tomuto seznamu vypište součet hodnot všech vylosovaných karet. Položme hodnotu karet J, Q a K rovnu deseti a eso rovnu jedné.

vybrane_karty = []
vybrana_karta_1 = f'{random.choice(karty)} {random.choice(barvy)}'
vybrana_karta_2 = f'{random.choice(karty)} {random.choice(barvy)}'
vybrana_karta_3 = f'{random.choice(karty)} {random.choice(barvy)}'
vybrana_karta_4 = f'{random.choice(karty)} {random.choice(barvy)}'
vybrane_karty.append(vybrana_karta_1)
vybrane_karty.append(vybrana_karta_2)
vybrane_karty.append(vybrana_karta_3)
vybrane_karty.append(vybrana_karta_4)

print(vybrane_karty)

hodnoty_karet = {
    'kluk': 10,
    'dáma': 10,
    'král': 10,
    'eso': 1,
}

seznam_hodnot = []
soucet_hodnot = 0

for karta in vybrane_karty:
    karta = karta.split()
    seznam_hodnot.append(karta[0])
    
for hodnota in seznam_hodnot:
    if hodnota in hodnoty_karet:
        hodnota = hodnoty_karet[hodnota]
        soucet_hodnot += hodnota
    else:
        soucet_hodnot += int(hodnota)

print(soucet_hodnot)
