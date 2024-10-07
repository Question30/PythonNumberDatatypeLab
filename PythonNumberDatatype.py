'''
 1. Write a Python program that declares two integer variables, assigns an integer to each, and adds them together. Assign the sum to a variable. Print out the result.
'''
num1 = 5
num2 = 3
sum = num1 + num2
print("The sum is: " , sum);

'''
2. Write a Python program that declares two float variables, assigns a number to each, and adds them together. Assign the sum to a variable. Print out the result.
'''
num1 = 2.5
num2 = 7.10
sum = num1 + num2
print("The sum is :", sum)

'''
3.Write a Python program that declares an integer variable and a float variable, assigns numbers to each, and adds them together. Assign the sum to a variable. Print out the result. What variable type must the sum be? (Hint: The variable type of the sum must be a float).
'''

num1 = 10
num2 = 13.7
sum = float(num1) + num2
print("The sum is : ", sum)

'''
4.Write a Python program that declares two integer variables, assigns an integer to each, and divides the larger number by the smaller number. Assign the result to a variable. Print out the result. 
'''

num1 = 40
num2 = 2
result = num1 / num2
print("The result is : ", result)

'''
5.Write a Python program that declares two float variables, assigns a number to each, and divides the larger by the smaller number. Assign the result to a variable. Print out the result. 
'''
num1 = 10.5
num2 = 3.3
result = num1 / num2
print("The result is: ", result)

'''
6.Write a program where you create three variables that represent products at a cafe. The products could be beverages such as `coffee,` `cappuccino,` `espresso,` `green tea,` etc. Assign prices to each product.
'''

coffee = 5.00
capuccino = 7.00
green_tea = 4.00

'''
7.Create two more variables called subtotal and totalSale, and complete an “order” for three items of the first product, four items of the second product, and two items of the third product. Add them all together to calculate the subtotal. Create a variable called SALES_TAX and add sales tax to the subtotal to obtain the totalSale amount.
'''

subtotal = (3 * coffee) + (4 * capuccino) + (2 * green_tea)
SALES_TAX = subtotal * 0.8
totalSale = subtotal + SALES_TAX
print("Total: ", totalSale)

'''
8.Write a Python program that calculates the area of a circle based on the radius = 63. To calculate the area of a circle based on the radius, we can use the following formula
'''

radius = 63
pi = 3.14
area = pi * radius**2
print("Area :", area)