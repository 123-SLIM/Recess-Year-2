#1
names = ["Aaron","Lema","Edgar","Tumusiime","Anold"]
print(names[1])

#3
print(names.append("Nelson"))
print(names)
#4
print(names.append(2,"Bathel"))
#8
countries = ["Uganda","Tanzania","Kenya"]
countries_copy = countries.copy()
print(countries)
print(countries_copy)

#10
animals = ["cat","dog","rabbit","sheep"]
animals_sort = animals.sort()
print(animals_sort)
animals_sort_rev= animals.sort(reverse=True)
print(animals_sort_rev)


#tuples
#1
x = ("samgung", "iphone", "tecno", "redmi")
print(x[1])
#2
print(x[-2])
#3
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)
#5
for phone in x:
    print(phone)
#6
x = x[1:]   
print(x)
#7
towns = tuple(["Kampala","Entebbe", "Jinja" "Mbarara"])
print(towns)
#8
a,b,c,d = towns
print(a)
#10
first_name = ("Aaron", "John" "Micheal")
second_name = ("Joe", "Junior", "Gilbert")
full_name = first_name = second_name
print(full_name)
#11
colors = ("red","blue","green")
multiplied_colors = colors*3
print(multiplied_colors)
#12
tuple = (1,3,7,8,7,5,4,6,8,5)
count_eight = tuple.count(8)
print(count_eight)
#dictionary
shoes = {
    "brand": "nick",
    "color":"black",
    "size": 40, 
}
#2
print(shoes.update({"brand":"Adidas"}))
#4
print(shoes.key())
#5
print(shoes.values())
#6
if "size" in shoes.keys():
    print("yes")
else:
    print("no")
#7
for i in shoes:
    print(shoes[i])
#8
shoes.pop("color")
print(shoes)
#9
shoes.clear()
print(shoes)
#10
number_word ={
   1:"one",
   2:"two",
   3:"three",
   4:"four",
   5:"five",
}
number_copy = number_word.copy()
print(number_copy)
print(number_word)
#11
my_family = {
    "child1":{
        "name": "Aaron",
        "year": 2020,
    },
    "child2":{
        "name": "Nelson",
        "year": 2021,
    } 
}
print(my_family["child1"]["name"])
#looping through nested dictionary
for x in my_family:
    for y in my_family[x]:
        print(my_family[x][y])