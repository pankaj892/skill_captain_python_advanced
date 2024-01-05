'''Importing math_operations module and using its functions'''
import math_operations

''' Ask the user to enter two numbers and store them in variables a and b'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

'''Print the results of the operations'''
'''We are using the functions from the math_operations module'''
print("Addition: ", math_operations.add_operation(a, b))
print("Subtraction: ", math_operations.subtract_operation(a, b))
print("Multiplication: ", math_operations.multiply_operation(a, b))
print("Division: ", math_operations.divide_operation(a, b))
print("Modulo: ", math_operations.modulo_operation(a, b))
print("Power: ", math_operations.power_operation(a, b))
print("Floor Division: ", math_operations.floor_division_operation(a, b))
