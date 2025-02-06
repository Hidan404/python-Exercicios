
while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if not isinstance(nota, int):
            print("Por favor, digite um número inteiro.")
            continue

        if nota >= 0 and nota <= 10:
            print(f"Nota valida {nota}")
            break
        else:
            print("nota invalida")
    except ValueError:  
        print("tipo de dado invalido")      
           

