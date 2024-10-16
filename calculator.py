
def circle(r):
    PI = 3.141
    r = int(input("Enter radius of circle: "))
    
    return PI*r**2

# To import this function in an other script, simply call the module by using from and import the function by using import
# Ex.  from calculator import circle
# To use the module, call it's function "circle", which takes one parameter
#Ex. circle(int(input())) will call the function and pass on a user inputted integer to calculate the area of a circle
