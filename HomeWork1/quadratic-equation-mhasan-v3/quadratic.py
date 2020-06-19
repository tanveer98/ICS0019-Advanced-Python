'''
Function to calculate to solution(s) of q quadratic equation in the form of ax^2+bx+c
@param a: int
@param b: int
@param c: int
@return a tuple containing x1 and x2, or an empty tuple if solution could not be calculated.
'''
from math import sqrt
def calculate(a,b,c):
    if(a == 0):
        return ()
    discriminant = (b*b) - (4*a*c)
    if(discriminant < 0):
        return ()
    x1 = ( -b + sqrt(discriminant) ) / (2 * a)
    x2 = ( -b - sqrt(discriminant) ) / (2 * a)
    return (x1,x2)

if __name__ == "__main__":
    sol = calculate(a=1,b=4,c=3)
    print(sol)