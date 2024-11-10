# # Vlož si následující kód do editoru a splň úkol v komentáři

cislo = 100
print(cislo)

# # Sem přidej kód, který proměnnou cislo zvýší o 1
cislo = cislo + 1

print(cislo)  # Vypíše 101

# # Ulož do proměnné cislo vstup od uživatele
# # cislo =
cislo = int(input('Zadej číslo: '))
print(cislo)  # Zopakuje zadanou hodnotu

# # Sem přidej kód, který proměnnou cislo zvýší o 1
cislo = cislo + 1

print(cislo)  # Vypíše cislo zvětšené o 1

# Pokud pečete podle anglických receptů, často se po váš požaduje rozehřát troubu na uvedenou teplotu. 
# Pokud si ovšem neuvědomíte, že Američané používají pro měření teploty stupně Fahrenheita namísto Celsia, bude vás na konci pečení čekat nemilé překvapení.

# Nastudujte si na České Wikipedii jak se převádějí stupně Fahrenheita na stupně Celsia a napište program, který takový převod provede. 
# Váš program se zeptá uživatele na teplotu ve stupních Fahrenheita a vypíše její ekvivalent ve stupních Celsia.

fahrenheit = input('Zadej teplotu (Fahrenheit): ')

try:
    fahrenheit = float(fahrenheit)
    fahrenheit_to_celsius = (5 * (fahrenheit - 32) / 9)
    print(f'vámi zadaná teplota je {fahrenheit_to_celsius} °C')
except ValueError:
    print(f'Vámi zadaná hodnota {fahrenheit} neodpovídá žádanému formátu. ')

# Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum()).

seznam_cisel = [1, 3, 8, 98, 115, 2, 3, 115, 98, 55, 136]

soucet = 0
for num in seznam_cisel:
    soucet += num
    
print(soucet)

# Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max()).

max_number = seznam_cisel[0]

for num in seznam_cisel:
    if num > max_number:
        max_number = num
        
print(max_number)

# Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu.

# Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam se sudými čísly a nový seznam s lichými čísly z původního seznamu.
licha_cisla = []
suda_cisla = []
for num in seznam_cisel:
    if num % 2 == 0:
        suda_cisla.append(num)
    else:
        licha_cisla.append(num)
        
print(suda_cisla, licha_cisla)

# Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů. Výsledné pořadí prvků musí být zachováno.

unique_nums = []

for num in seznam_cisel:
    if num not in unique_nums:
        unique_nums.append(num)
        
print(unique_nums)

# Vrať se k příkladu vysvědčení studenta.

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
# # Při přihlašování na střední školu mohou být důležitější příklady z některých konkrétních předmětů. Uprav kód z lekce tak, aby spočítal průměr pouze z jazyků, matematiky a fyziky.

important_subjects = ['Český jazyk', 'Anglický jazyk', 'Matematika', 'Fyzika']
marks = []

for subject in school_report:
    if subject[0] in important_subjects:
        marks.append(subject[1])
        
average_mark = sum(marks) / len(marks)

print(average_mark)
       
    
# V následujícím seznamu máš seznam rodných čísel pacientů, kteří navštívili v jeden konkrétní den lékařskou ordinaci.

rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]
# Kolik přišlo mužů a kolik žen?
# Kdy se narodil nejstarší a kdy nejmladší pacient?
# Pokud nevíš, jak funguje rodné číslo, vysvětlení je níže:

# Rodné číslo je identifikační číslo, které slouží k jednoznačné identifikaci osoby. V České republice se rodné číslo skládá z 10 číslic a jednoho lomítka, 
# které ho rozděluje na části.

# Prvních 6 číslic udává datum narození v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice). 
# Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202. Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby.
# Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě. 

def get_birthday(rc):
    rocnik = int(rc[0:2])
    if rocnik > 25:
        plny_rok = 1900 + rocnik
    else:
        plny_rok = 2000 + rocnik
    mesic = int(rc[2:4]) % 50
    den = rc[4:6]
    birthday = f'{den}. {mesic}. {plny_rok}'
    return birthday  
    

seznam_zeny = []
seznam_muzi = []
nejmladsi_rc = rodna_cisla[0]
nejstarsi_rc = rodna_cisla[0]


for num in rodna_cisla:
    rocnik = int(num[0:2])
    if rocnik > 25:
        plny_rok = 1900 + rocnik
    else:
        plny_rok = 2000 + rocnik
    mesic = int(num[2:4]) 
    den = int(num[4:6])
    if mesic >= 50:
        seznam_zeny.append(num)
        mesic = mesic - 50
    else:
        seznam_muzi.append(num)
    if int(nejmladsi_rc[0:2]) > 25:
        nejmladsi_rok = 1900 + int(nejmladsi_rc[0:2])
        nejstarsi_rok = 1900 + int(nejstarsi_rc[0:2])
    else:
        nejmladsi_rok = 2000 + int(nejmladsi_rc[0:2]) 
        nejstarsi_rok = 2000 + int(nejstarsi_rc[0:2]) 
    
    nejmladsi_mesic = int(nejmladsi_rc[2:4]) % 50
    nejstarsi_mesic = int(nejstarsi_rc[2:4]) % 50
    nejmladsi_den = int(nejmladsi_rc[4:6])
    nejstarsi_den = int(nejstarsi_rc[4:6])    
    if plny_rok > nejmladsi_rok or (plny_rok == nejmladsi_rok and mesic > nejmladsi_mesic) or (plny_rok == nejmladsi_rok and mesic == nejmladsi_mesic and den > nejmladsi_den):
        nejmladsi_rc = num
    if plny_rok < nejstarsi_rok or (plny_rok == nejstarsi_rok and mesic < nejstarsi_mesic) or (plny_rok == nejstarsi_rok and mesic == nejstarsi_mesic and den < nejstarsi_den):
        nejstarsi_rc = num
    


                    

 
pocet_zen = len(seznam_zeny)
pocet_muzu = len(seznam_muzi)

print(f'Pocet zen v ordinaci byl {pocet_zen}')
print(f'Pocet muzu v ordinaci byl {pocet_muzu}')
print(f'Datum narozeni nejmladsiho pacienta bylo {get_birthday(nejmladsi_rc)}. ')
print(f'Datum narozeni nejstarsiho pacienta bylo {get_birthday(nejstarsi_rc)}. ')