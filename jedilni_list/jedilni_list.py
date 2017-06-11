# -*- coding: utf-8 -*-

print u"Pozdravljeni v programu za dnevni meni."

menu = {}

while True:
    ime_jedi = raw_input(u"Vpišite jed: ")
    cena = raw_input(u"Vpišite ceno jedi: " )
    cena = int(cena)
    menu[ime_jedi] = cena

    nova_jed = raw_input("Ali bi dodali novo jed? (y/n) ")

    if nova_jed == "n":
        break

with open("menu.txt", "w") as menu_file:
    for ime_jedi in menu:
        menu_file.write("{0}: {1} EUR\n".format (ime_jedi, cena))

print menu