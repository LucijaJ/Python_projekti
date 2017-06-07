# -*- coding: utf-8 -*-

print u"Pozdravljeni! To je pretvornik enote, ki pretvarja kilometre v milje."

while True:
    print u"Vnesite število kilometrov, ki bi jih radi spremenili v milje."
    km = raw_input("Kilometri: ")

    km = int(km) # ustvari novo realno število iz celega števila ali niza znakov
    milje = km * 0.621371

    print "{0} kilometrov je {1} milj.".format(km, milje)

    vprasanje = raw_input (u"Ali želite narediti novo pretvorbo? (da/ne): ")

    if vprasanje.lower() != "d" and vprasanje.lower() != "da":
        break