# # Mějme seznam pohybů na nějakém bankovním účtu:

pohyby = [1200, -250, -800, 540, 721, -613, -222]
# # Vypište v pořadí třetí pohyb z uvedeného seznamu.
# # Vypište všechny pohyby kromě prvních dvou.
# # Vypište kolik je všech pohybů dohromady.
# # Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# # Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.

treti_pohyb = pohyby[2]
pohyby_od_tretiho = pohyby[2:]
pocet_pohybu = len(pohyby)
min_pohyb = min(pohyby)
max_pohyb = max(pohyby)
prirustek = sum(pohyby)

print(treti_pohyb)
print(pohyby_od_tretiho)
print(pocet_pohybu)
print(min_pohyb)
print(max_pohyb)
print(prirustek)

# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.

s = [1, 6, 89, 133, 54, 98, 45, 46]

if len(s) > 0:  
    prumer = sum(s) / len(s)
else:
    print('Seznam je prázdný. ')

print(prumer)

# # Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.

rozpeti = max(s) - min(s)

print(rozpeti)

# # Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# # U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.



index_stred = len(s) // 2
stredni_cislo = s[index_stred]

print(stredni_cislo)

# # Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# # Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.

index_stred_mensi = (len(s) -1) // 2
stred_mensi = s[index_stred_mensi] 

print(stred_mensi)

# Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

jmeno = 'Radka'

velka = jmeno.upper()
mala = jmeno.lower()

print(velka, mala)

# Mějme seznam celých čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']
# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

hodnoty = ['12', '1', '11', '-11']

hodnoty[2] = int(hodnoty[2]) + 4

print(hodnoty)

# Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu, ale v řetězci oddělená mezerou:

hodnoty = '12.1 1.68 7.45 -11.51'
# # K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto

hodnoty = '12.1 1.68 7.45 -11.26'
# # Určitě se vám budou hodit metody split a join.

hodnoty = hodnoty.split()
hodnoty[-1] = str(float(hodnoty[-1]) + 0.25)
hodnoty = ' '.join(hodnoty)
print(hodnoty)

# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

import math

cislo = float(input('Zadej desetinné číslo: '))

nahoru = math.ceil(cislo)
dolu = math.floor(cislo)
bezne = round(cislo)

print(nahoru, dolu, bezne)

# Uvažujme vysvědčení studenta, které máme uložené jako seznam.

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
# Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru. Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika. 
# Vypočítej průměr studenta z daných předmětů s využitím modulu statistics. 
# Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů. Nakonec použij metodu statistics.mean() k výpočtu průměru. 
# Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů.
# import statistics

# # important_subjects = ['Český jazyk', 'Anglický jazyk', 'Matematika', 'Fyzika']
# # important_marks = []

# # for subject in school_report:
# #     if subject[0] in important_subjects:
# #         important_marks.append(subject[1])
        
# # avg_mark = statistics.mean(important_marks)
# # best_mark = min(important_marks)
# # worst_mark = max(important_marks)

# # print(avg_mark, best_mark, worst_mark)

# Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu v datech. V modulu statistics existuje funkce mode(), která umí modus spočítat. 
# Funkce mode() má navíc vychytávku, umí pracovat i s řetězci.

# Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, jakou akci podniknou během jejich vánočního večírku. 
# Použij funkce mode() ke zjištění, pro jakou aktivitu hlasovalo nejvíce zaměstnanců. Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek.

votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]
# # Můžeš se podívat i na popis funkce v dokumentaci, která obsahuje i příklad s použitím řetězců.

best_activity = statistics.mode(votes)
print(best_activity)

retezec = 'abrakadabra'
best = statistics.mode(retezec)

print(best)

# Následující tabulka obsahuje průměrné roční teploty v České republice za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).

# rok	teplota °C
# 2001	7.8
# 2002	8.7
# 2003	8.2
# 2004	7.8
# 2005	7.7
# 2006	8.2
# 2007	9.1
# 2008	8.9
# 2009	8.4
# 2010	7.2

# Vytvořte reprezentaci této tabulky pomocí seznamu seznamů. Zde existují dvě možnosti. 
# Nejprve vytvořte seznam, který obsahuje řádky tabulky jako dvouprvkové seznamy a uložte jej do proměnné radky. 
# Poté vytvořte seznam, který obsahuje sloupce tabulky, tedy dva seznamy po deseti prvcích. Uložte jej do proměnné sloupce.

# Pro obě tyto reprezentace vyřešte následující úkoly

# Získejte teplotu na třetím řádku tabulky.
# Získejte rok na pátém řádku tabulky.
# Získejte poslední řádek tabulky jako seznam.
# Vytvořte tabulku bez prvních dvou řádků.
# Vytvořte tabulku pouze z prvních dvou řádků.
# Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
# Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.

radky = [
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
]


roky = []
teploty = []

for row in radky:
    roky.append(row[0])
    teploty.append(row[1])  

sloupce = [roky, teploty]
teploty_vzestupne = sorted(sloupce[1])


print(radky[2][1])
print(radky[4][0])
print(radky[-1])
print(radky[2:])
print(radky[0:2])
print(radky[4:8])
print(teploty_vzestupne)

# Máme data o písemce, která obsahovala 4 otázky. Za každou otázku mohl student (studentka) získat max. 10 bodů. 
# Výsledky studentů jsou v následující tabulce.

# Student	Otázka 1	Otázka 2	Otázka 3	Otázka 4
# A	9	7	8	5
# B	5	3	6	6
# C	8	4	9	7
# D	8	5	4	8
# E	10	6	10	7
# Ulož si známky studentů do dvourozměrného seznamu.

# Spočítej známku jednotlivých studentů. Známku urči podle celkového počtu bodů ze všech příkladů. Bodovací tabulku najdeš níže.

# Body	Známka
# 36 a více	1
# 32 a více	2
# 26 a více	3
# 20 a více	4
# méně než 20	5
# Vypočítej průměrné body z jednotlivých otázek. Ze které otázky dostali studenti v průměru nejvíce bodů? A ze které naopak nejméně?

import statistics

tabulka_body = [
    ["A", 9, 7, 8, 5],
    ["B", 5, 3, 6, 6],
    ["C", 8, 4, 9, 7],
    ["D", 8, 5, 4, 8],
    ["E", 10, 6, 10, 7]
    ]

for student in tabulka_body:
    celkem_bodu = sum(student[1:])
    if celkem_bodu >= 36:
        znamka = 1
    elif 32 <= celkem_bodu < 36:
        znamka = 2
    elif 26 <= celkem_bodu < 32:
        znamka = 3
    elif 20 <= celkem_bodu < 26:
        znamka = 4
    else:
        znamka = 5
    print(f'Student {student[0]} získal celkem {celkem_bodu} bodů, byl ohodnocen známkou {znamka}. ')
    
body_otazka_1 = []
body_otazka_2 = []
body_otazka_3 = []
body_otazka_4 = []

for student in tabulka_body:
    body_otazka_1.append(student[1])
    body_otazka_2.append(student[2])
    body_otazka_3.append(student[3])
    body_otazka_4.append(student[4])
    
prumer_otazka_1 = statistics.mean(body_otazka_1)
prumer_otazka_2 = statistics.mean(body_otazka_2)
prumer_otazka_3 = statistics.mean(body_otazka_3)
prumer_otazka_4 = statistics.mean(body_otazka_4)

prumery = [prumer_otazka_1, prumer_otazka_2, prumer_otazka_3, prumer_otazka_4]

prumer_na_otazku = {}
prumer_na_otazku['1'] = prumer_otazka_1
prumer_na_otazku['2'] = prumer_otazka_2
prumer_na_otazku['3'] = prumer_otazka_3
prumer_na_otazku['4'] = prumer_otazka_4

nejlepsi_prumer = prumer_na_otazku['1']
nejlepsi_otazka = ''
nejhorsi_prumer = prumer_na_otazku['1']
nejhorsi_otazka = ''

for otazka, prumer in prumer_na_otazku.items():
    if prumer > nejlepsi_prumer:
        nejlepsi_prumer = prumer
        nejlepsi_otazka = otazka
    if prumer < nejhorsi_prumer:
        nejhorsi_prumer = prumer
        nejhorsi_otazka = otazka
        
print(f'Průměr otázky 1: {prumer_otazka_1}. ')
print(f'Průměr otázky 2: {prumer_otazka_2}. ')  
print(f'Průmět otázky 3: {prumer_otazka_3}. ')
print(f'Průměr otázky 4: {prumer_otazka_4}. ')     
print(f'Nejlépe hodnocená byla otázka {nejlepsi_otazka} s průměrným počtem bodů {nejlepsi_prumer} bodů. ')
print(f'Nejhůře hodnocená byla otázka {nejhorsi_otazka} s průměrným hodnocením {nejhorsi_prumer} bodů. ')


# Níže máš seznam akcí, které se konaly v zasedačce jedné firmy.

akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
# # Napiš program, který zjistí následující:

# # Kolik se uskutečnilo pohovorů?
# # V jakých jazycích se mohou zaměstnanci firmy vzdělávat?
# # Při řešení můžeš využít operátor in a slicing, případně metodu split()

pocet_pohovoru = 0
seznam_jazyku = []

for a in akce:
    if 'pohovor' in a:
        pocet_pohovoru += 1
    if 'jazykový' in a:
        a = a.split('-')
        jazyk = a[1].strip()
        if jazyk not in seznam_jazyku:
            seznam_jazyku.append(jazyk)
        
print(pocet_pohovoru)
print(seznam_jazyku)

# Stříbrná medaile je sice úžasný úspěch, ale kdo by nechtěl vyhrát? Podívejme se, kolik chybělo stříbrnému běžci k vítězství.

# Nejprve si vytvoř dvě proměnné, do kterých ulož čas vítěze a čas závodníka se stříbrnou medailí. Oba časy převeď na minuty a ulož jako číslo.
# Vypočti rozdíl obou proměnných. Tím zjistíš, kolik minut chybělo stříbrnému závodníku k vítězství.

vysledky = [
    ["Brunner Radek", [3, 0, 9]], 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]

time_winner = vysledky[0][1]
time_silver = vysledky[1][1]

time_winner_min = (time_winner[0] * 60) + time_winner[1] + (time_winner[2] / 60)
time_silver_min = (time_silver[0] * 60) + time_silver[1] + (time_silver[2] / 60)

dif_min = time_silver_min - time_winner_min 

print(f'Závodníkovi, který se umístil na druhém místě, chybělo k vítězství {dif_min:.2f} minut. ')

# Zadání je podobné jako u předchozího příkladu, ale nyní zkusíme výpočet provést pro všechny závodníky.

# Nejprve (pomocí cyklu a metody append()) vytvoř dvourozměrný seznam, 
# kde na nulté pozici vnořeného seznamu je číslo běžce a na první pozici je čas běžce v minutách jako desetinné číslo.
# Ve druhém kroku (opět pomocí cyklu a metody append()) vytvoř další dvourozměrný seznam, 
# kde na nulté pozici vnořeného seznamu je číslo běžce a na první pozici je rozdíl času běžce oproti času vítěze v minutách. 
# Jinak řečeno, bude tam číslo, které udává, o kolik by běžec musel být rychlejší, aby závod vyhrál.

vysledky_min = []

for index, zavodnik in enumerate(vysledky, start=1):
    runner = []
    position = index
    time = zavodnik[1]
    time_min = round((time[0] * 60) + time[1] + (time[2] / 60), 2)
    runner.append(position)
    runner.append(time_min)
    vysledky_min.append(runner)
    
print(vysledky_min)

winner_time_min = vysledky_min[0][1]
vysledky_dif_min = []


for zavodnik in vysledky_min:
    runner_dif = []
    name = zavodnik[0]
    dif_min = round(zavodnik[1] - winner_time_min, 2)
    runner_dif.append(name)
    runner_dif.append(dif_min)
    vysledky_dif_min.append(runner_dif)
    
print(vysledky_dif_min)    