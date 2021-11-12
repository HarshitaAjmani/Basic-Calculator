print("\n\n\t*** BASIC CALCULATOR *** ")
print('''\n1.Addition
2.Subtraction
3.Multiplication
4.Division''')

opp = int(input("\nSelect the operation you want to perform: " ))
num_1 = int(input("First Number: "))
num_2 = int(input("Second Number: "))

if (opp == 1 ):
    print(num_1," + ",num_2," = ", (num_1 + num_2) )
elif (opp == 2 ):
    print(num_1," - ",num_2," = ", (num_1 - num_2) )
elif (opp == 3 ):
    print(num_1," X ",num_2," = ", (num_1 * num_2) )
elif (opp == 4 ):
    print(num_1," / ",num_2," = ", (num_1 / num_2) )
