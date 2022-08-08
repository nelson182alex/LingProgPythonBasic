

def calcularDivisores(num):
    for n in range(1 , num):
        if num%n == 0:
            print(n)

calcularDivisores(100)