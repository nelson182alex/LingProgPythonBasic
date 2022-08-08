def calcularFatorial(numero):
    resultado=1
    count=1
    while count <= numero:
        resultado *= count
        count += 1

    print(resultado)

calcularFatorial(10)
    