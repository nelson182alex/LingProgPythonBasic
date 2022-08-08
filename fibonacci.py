
def calcularFibonacci(n):
    ultimo=1
    penultimo=1
    if (n==1) or (n==2):
        print("1")
    else:
        print("1")
        print("1")
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            print(termo)


calcularFibonacci(10)

    