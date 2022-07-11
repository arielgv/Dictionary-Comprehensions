#Another task this time involving some of 'dictionary comprehensions', it is a practice session only.


my_dict = {
    "France" : "Europe",
    "China" : "Asia",
    "Portugal": "Europe",
    "USA": "America",
    "Egypt": "Africa",
    "Brasil": "America",
    "Spain": "Europe",
    "Argentina": "America"
}

print('The dictionary contains:', my_dict)

only_america = { x:v for (x,v) in my_dict.items() if v== "America"}


list_america = [ x for (x,v) in my_dict.items() if v=="America" ]
#This line useas a list comprehension tool only of keys which values were "America"



print('Ditionary example:',only_america,"\n", 'List example:',list_america)


# Practice for double a value in a new dictionary

my_dict = { "a":1,"b":2,"c":3, "d":4, "e":5}
print(my_dict)
doublevalue = {x:v*2 for (x,v) in my_dict.items()}
print(doublevalue)
