# -*- coding: utf-8 -*-

print "To je FizzBuzz igrica"

stevilka = raw_input(u"Izberi številko med 1 in 100: ")

stevilka = int(stevilka)

for num in range(1, stevilka+1):
    if num % 3 == 0 and num % 5 == 0:
        print "fizzbuzz"
    elif num % 3 == 0:
         print "fizz"
    elif num % 5 == 0:
        print "buzz"
    else:
        print num
