
#functions

def squaregame(number):
    print("This is use to square numbers")
    return number ** 2

squaregame(10)

def allowed_dating_age(my_age):
    girl_age = my_age / 2 + 7
    return girl_age
tmuw3h_limits = allowed_dating_age(23)

print("tmuw3h you can date girls that are " + str(tmuw3h_limits), " or older")

#default arguement values

def gender(sex = 'unknown'):
    if sex is 'm':
        print("you selected Male")
    elif sex is 'f':
        print('you selected Female')
    else: print("You did not enter any gender so we put ", str(sex))

gender()
gender("m")
gender("f")

#key word awesome
print("\n#compliment function")
def compliments(name = "tmuweh", action="is", adjectiv = "awesome"):
    print(name," ", action," ", adjectiv)

compliments()
compliments(name = "Tangue")
compliments(action = "was")
compliments(adjectiv="great!")

#Flexible number of arguments

print("\n#Flexible number of arguments")

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(str(total))

add_numbers(40, 40)

add_numbers(1 , 2, 3, 4 , 5, 6, 7, 8)
add_numbers(3, 90, 8, 50, 7)
add_numbers(0)

