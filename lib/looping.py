#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10

    while count > 0:
        print(count)
        count -= 1

    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    int_list = [val * val for val in int_list]
    
    return int_list
        
def fizzbuzz():
    # code goes here!
    for val in range(1, 101):
        if val % 3 == 0 and val % 5 == 0:
            print("FizzBuzz")
        elif val % 3 == 0:
            print("Fizz")
        elif val % 5 == 0:
            print("Buzz")
        else:
            print(val)

