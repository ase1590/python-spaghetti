import time

letters = "we gonna divide some stuff"
n1="type first number: "
n2="type second number to divide by: "

print(letters)

a=float(input(n1))
b=float(input(n2))

# ##### DONT TOUCH ANYTHING BELOW LINE #####
# #####  IT WORKS AND I DONT KNOW WHY  #####
add_used = 0

# define add
def add(a, b):
    global add_used
    add_used += 1
    return a + b

# dont know why this works but it does.
def divide(a, b):
    quotient = 0
    c = 0
    d = 0
    while add(d, b) <= a:
        c = add(c, 1)
        d = add(d, b)
    return c

print("the answer is: ",divide(a, b))

time.sleep(3)
