# determining the length of a string.
a = "Manchester United"
b = len(a)
print(b)

#slicing in strings
name = "Eric Ten Hag"
my_name = name[5:8:1]
print(my_name)

# arithmetic operartions with numbers
x = 10
y = 15
w = (15-10)/5
print(w)
#iterating through each character of a string using a for loop
name = "Marcus Rashford" 
for i in name:
     print(i)
#using boolean values and conditons to control programs

my_age = 23
her_age= 22
if her_age > my_age:
    print(False)
else: print( True)
# Dictionary(Using the value method)
capitals = {
    "Uganda":"Kampala", "Kenya":"Nirobi", "Tanzania":"Mombasa"
}
values = capitals.values()
for value in values:
    print(value)
    #changing and updating items in a dictionary
    capitals = {
    "Uganda":"Kampala", "Kenya":"Nirobi", "Tanzania":"Mombasa"
}
capitals.update({"Egypt":"Cairo"})
capitals.update({"Tanzania":"Dar-El-Salaam"})
print(capitals)
# adding and removing items from the dicionary
capitals = {
    "Uganda":"Kampala", "Kenya":"Nirobi", "Tanzania":"Mombasa"
}
capitals.pop("Uganda")
print(capitals)
# looping through a dictionary
capitals = {
    "Uganda":"Kampala", "Kenya":"Nirobi", "Tanzania":"Mombasa"
}
for things in capitals:
    print(things, "->",capitals[things])

    