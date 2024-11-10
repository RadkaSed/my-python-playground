# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
    return a * b 

# Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. 
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

# def total_price(persons, breakfast=False):
#     price_for_night = 850
#     price_for_breakfast = 125
#     if breakfast:
#         price = persons * (price_for_night + price_for_breakfast)
#     else:
#         price = persons * price_for_night
#     return price

# print(total_price(3)) 
# print(total_price(3, True))

# Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.

numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# Návod:

# Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
# Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami
# Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat
# Výstup:

#      7728
#        88
#    958621
#      5941
# 959847272
#      3944
#        80
#       521
#     57035
#   3967894
# Výstup bonusu:

# .....7728
# .......88
# ...958621
# .....5941
# 959847272
# .....3944
# .......80
# ......521
# ....57035
# ..3967894

# char_number = len(str(numbers[0]))


# for num in numbers:
#     if len(str(num)) > char_number:
#         char_number = len(str(num))
       
           

# def fill_char(retezec, number, znak=' '):
#     fill_string = znak * (number - len(retezec)) + retezec
#     return fill_string

# for num in numbers:
#     num = str(num)
#     print(fill_char(num, char_number, znak='*'))


# Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

# první řada (hodnoty 1, 4, 7 atd.),

# druhá řada (hodnoty 2, 5, 8 atd.),

# třetí řada (hodnoty 3, 6, 9 atd.).

# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. 
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. Vyhodnoť, do které řady číslo náleží. 
# Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.

# Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.

# import random

# def generate_line(start):
#     return list(range(start, 37, 3))

# def roulette(line_num, bet):
#     number = random.randint(0, 36)
#     line_1 = generate_line(1)
#     line_2 = generate_line(2)
#     line_3 = generate_line(3)
    
#     if number == 0:
#         print('Padla 0, prohráváte.')
#         return 0
#     elif (line_num == 1 and number in line_1) or (line_num == 2 and number in line_2) or (line_num == 3 and number in line_3):
#         print(f'Padlo číslo {number}, vyhráváte. ')
#         return bet * 2
#     else:
#         print(f'Padlo číslo {number}. Prohráváte.')
#         return 0
        
# line_num = int(input('Zadejte číslo řady (1, 2, nebo 3): '))
# if line_num > 3 or line_num < 1:
#     print(f'Zadaný znak {line_num} neodpovídá žádanému formátu. ')
#     exit()
# bet = int(input('Zadejte výši sázky v Kč: '))
# if bet <= 0:
#     print(f'Neplatná výše sázky, zadejte kladné číslo. ')
#     exit() 

# prize = roulette(line_num, bet)
# print(f'Vyhráváte {prize} Kč. ')


# Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno. 
# Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.

# Nápověda: random.shuffle()

# Super bonus: Napiš program, který takovou funkci využije na delší text více slov.

text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
# '''
# Výstup:

# Slvoo je sátle mnžoé pdhlnooě pseířčt, když jsou pcnhíoamá psímnea. 
# Stčaí, kydž pvrní a ponsldeí pmínseo je na své pozcii znaáhvoco. Nipaš fcnkui, 
# kretá bude mít jkao vsntpuí paaremtr solvo a vátrí solvo, kde zhpezáří všhecny 
# zanky krmoě pírhnvo a plísoednho.

# import random

# def michanice(slovo):
#     if len(slovo) <= 3:
#         return slovo 

#     middle_chars = list(slovo[1:-1]) 
#     random.shuffle(middle_chars)
#     shuffled_word = slovo[0] + ''.join(middle_chars) + slovo[-1]
#     return shuffled_word


# text_list = text.split()
# text_list_shuffle = []

# for slovo in text_list:
#     stripped_word = slovo.strip(",.?!")
#     if len(stripped_word) > 1:
#         shuffled = michanice(stripped_word)
#         if slovo[-1] in ",.?!":
#             shuffled += slovo[-1]
#         text_list_shuffle.append(shuffled)
#     else:
#         text_list_shuffle.append(slovo) 

# shuffled_text = ' '.join(text_list_shuffle)
# print(shuffled_text)

# Náprava je část vozidla, která spojuje kola s karosérií vozidla. U nákladních vozidel ho můžeme chápat jako počet "dvojic kol". 
# Počet náprav je důležitý napříkad kvůli maximální povolené hmotnosti vozidla.

# Uvažuj limity pro maximální hmotnost nákladního vozidla, které jsou v tabulce níže.

# Počet náprav	Maximální dovolená hmotnost v tunách
# 2	18
# 3	25
# 4	32
# 5	48
# Pokud je limit překročen, platí provozovatel pokutu 1000 Kč za každou tunu, o které je vozidlo těžší. 
# Například pokud má vozidlo 4 nápravy a hmotnost 34 tun, platí provozovatel pokutu 2000 Kč. Napiš funkci spocitej_pokutu(), 
# která bude mít dva parametry - pocet_naprav (počet náprav vozidla) a hmotnost (hmotnost vozidla v tunách). 
# Funkce na základě těchto parametrů vypočte výši pokuty a vrátí ji jako celé číslo.

# pokuta = spocitej_pokutu(4, 34)
# print(pokuta) # 2000
# Dále uvažuj následující dvourozměrný seznam, kde na prvním místě vnořeného seznamu je počet náprav vozidla a na druhém místě je zjištěná hmotnost.

vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]

# Projdi seznam pomocí cyklu a pro každé vážení urči (s využitím funkce spocitej_pokutu()) výši pokuty. Spočítej celkovou výši pokut za všechna vážení.

# def spocitej_pokutu(pocet_naprav, hmotnost):
#     maximalni_povolene_hmotnosti = {2: 18, 3: 25, 4: 32, 5: 48}
#     if pocet_naprav not in maximalni_povolene_hmotnosti:
#         print('Neznámý počet náprav. ')
#         return 0
#     max_hmotnost = maximalni_povolene_hmotnosti[pocet_naprav]
#     if hmotnost > max_hmotnost:
#         rozdil = hmotnost - max_hmotnost
#         pokuta = rozdil * 1000
#         return pokuta
#     else:
#         return 0
    
# print(spocitej_pokutu(2, 36))
# pokuty = []

# for line in vazeni:
#     print(spocitej_pokutu(line[0], line[1]))
#     pokuty.append(spocitej_pokutu(line[0], line[1]))
    
    
# celkova_vyse_pokut = sum(pokuty)
# print(celkova_vyse_pokut)