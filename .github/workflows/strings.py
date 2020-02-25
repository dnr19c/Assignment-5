Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # We use the exec() function to execute any string as Python Code
>>> # Printing a string
>>> code = 'print("Hello World")'
>>> exec(code)
Hello World
>>> #Finding the product
>>> code = """
def product(num1, num2):
    return num1 * num2
print("The product is", product(2,3))
"""
>>> exec(code)
The product is 6
