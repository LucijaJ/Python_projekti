import random #random nikoli NE uporabljaj za fotke

while True:

    secret = random.randint (0, 100)

    print "Ugani skrito stevilo med 0 in 100 vkljucno."


    # for zanka:
    for stevec in range (5):
        answer = raw_input("Ugibaj: ")  # raw_input je vedno string!

        answer = int(answer) #spremenili smo string v int

        if answer == secret:
            print "Odgovoren je pravilen!"
            break
        elif answer > secret:
            print "Stevilka je previsoka, poizkusi znova."
        elif answer < secret:
            print "Stevilka je prenizka, poizkusi znova."
        # else:
        #     print "Napacen odgovor, poskusi ponovno, imas se ." + str(4 - stevec) + " poizkusov"

    print "Nisi uganil."

    odgovor = raw_input ("Ali zelis nadaljevati igro? (d/n)")
    if odgovor == "n":
        break













