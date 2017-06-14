import random #random nikoli NE uporabljaj za fotke

def main():
    secret = random.randint (0, 100)

    print "Ugani skrito stevilo med 0 in 100 vkljucno."

    while True:
        answer = int(raw_input("Ugani stevilo med 0 in 100: "))

        if answer == secret:
            print "Odgovoren je pravilen!"
            break
        elif answer > secret:
            print "Stevilka je previsoka, poizkusi znova."
        elif answer < secret:
            print "Stevilka je prenizka, poizkusi znova."

main()













