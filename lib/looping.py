#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0: 
        print(i)
        i = i-1
    print('Happy New Year!')
        
    

def square_integers(int_list):
     square_integers = [num * num for num in int_list]
     return square_integers
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i% 3==0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)
