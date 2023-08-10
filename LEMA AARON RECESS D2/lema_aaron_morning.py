# for loop
fruits = ["Mango", "Guava", "Orange"]
for fruit in fruits:
    print(fruit)
    # break statement
    for number in range(1,10):
        if number == 5:
            break
        print(number)
        # continue statement
        for number in range(1,10):
         if number == 5:
            continue
        print(number)
        
        