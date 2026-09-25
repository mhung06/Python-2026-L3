#ex1
r = float (input("Enter circle radius:") )
area = 3.14 * r * r 
print(f"Circle area ={area}")
#ex2
c = float (input("Enter the temperature in celsius:"))
f = c * 9/5 + 32
print(f"{c} (C)={f} (F)")
#ex3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number? "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")

#ex4    
def is_perfect(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


num = int(input("Enter a number? "))
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")

#ex5    
colors = ["Blue", "Yellow", "Black", "Red", "White"]
user_color = input("What is your favorite color? ")

if user_color in colors:
    print(f"Your color is at index {colors.index(user_color)} in my list")
else:
    print("Sorry, I could not find your color")
#ex6
range1 = list(range(0, 7))  # 0, 1, 2, 3, 4, 5, 6
range2 = list(range(1, 11, 3))  # 1, 4, 7, 10
range3 = list(range(5, 0, -1))  # 5, 4, 3, 2, 1
range4 = list(range(6, -3, -2))  # 6, 4, 2, 0, -2

print("range1:", ", ".join(map(str, range1)))
print("range2:", ", ".join(map(str, range2)))
print("range3:", ", ".join(map(str, range3)))
print("range4:", ", ".join(map(str, range4)))
#ex7
def remove_dollar_sign(s):
    return s.replace("$", "")
s = input("Enter a string: ")
print(remove_dollar_sign(s))
#ex8
def extract_event(l):
    return [x for x in l if x % 2 == 0]
l = [1,4,5,-1,10]
print(extract_event(l))
#ex9
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n =int(input("Enter a non-negative number:"))
print(f"{n}!= {factorial(n)}")
#ex10
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
n=int(input("Enter the Number:"))
print(f"V=Divisors of {n}: {get_divisors(n)}")
#ex11
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1, y1 = map(float, input("Enter point 1 (x y): ").split())
x2, y2 = map(float, input("Enter point 2 (x y): ").split())
print(f"Distance = {distance(x1, y1, x2, y2)}")
#ex12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            if n <= 2:
                print("* " * n)
            else:
                middle_spaces = "  " * (n - 2)
                print("* " + middle_spaces + "*")


m, n = map(int, input("Enter m n (rows cols): ").split())
print_pattern(m, n)                