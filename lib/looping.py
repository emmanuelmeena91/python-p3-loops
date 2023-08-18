#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i < 11:
        print(i)
        if (i == 1):
            print("Happy New Year!")
            break
        i -= 1
    pass


def square_integers(num_list):
    int_list = []
    for num in num_list:
        sqr = num * num
        int_list.append(sqr)
    return int_list

squared_numbers = square_integers([2, 4, 5, 6])


def fizzbuzzPrinter():
    
    for i in range(1 , 101):
       fizzbuzz(i)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

def reverseString(string):
    reversedstr = []
    for i in range(len(string)):
        reversedstr.append(string[i])

    reversedstr = ''.join(reversedstr)
    return reversedstr

reversed_string = reverseString("string")



print(reversed_string)        

        
fizzbuzzPrinter()      



happy_new_year()

print(squared_numbers)

