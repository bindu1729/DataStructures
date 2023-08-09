def greet():
    print("Hello")

greet()

def wish(firstname,lastname):
    print(f"Hello {firstname}  {lastname}")

wish("Gutta","Bindu")
wish(firstname="Sumanth",lastname="Nanduri")

def factorialofnumber(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"Factorial of {n} is {fact}")

factorialofnumber(5)

#O(n2)
def factorialofnumbers(n):
    for i in range(1,n+1):
        fact = 1
        for j in range(1,i+1):
            fact = fact * j
        print(f"Factorial is {fact}")


factorialofnumbers(5)

def factofnumbers(n):
    if n == 0:
        return 1
    fact = n*factofnumbers(n-1)
    return fact


#O(n2)
num = 5
fact_array = []
for n in range(0,num+1):
    fact_array.append(factofnumbers(n))
print(fact_array)





