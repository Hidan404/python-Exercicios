import random

dados_validos = []
identificador = 1

while True:
    try:
        usuario = {}  # Dicionário temporário para armazenar os dados de um usuário

        while True:
            nome = input("Digite seu nome: ").strip()
            if len(nome) > 3:
                usuario["Nome"] = nome
                break
            print("Erro: O nome deve ter mais de 3 caracteres.")

        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if 0 <= idade <= 150:
                    usuario["Idade"] = idade
                    break
                print("Erro: A idade deve estar entre 0 e 150.")
            except ValueError:
                print("Erro: Digite um número inteiro para a idade.")

        while True:
            try:
                salario = float(input("Digite seu salário: "))
                if salario >= 0:
                    usuario["Salário"] = salario
                    break
                print("Erro: O salário deve ser positivo.")
            except ValueError:
                print("Erro: Digite um valor numérico para o salário.")

        while True:
            sexo = input("Escolha 'M' ou 'F': ").upper().strip()
            if sexo in ['M', 'F']:
                usuario["Sexo"] = sexo
                break
            print("Erro: Sexo deve ser 'M' ou 'F'.")

        while True:
            estado_civil = input("Escolha [S] (Solteiro), [C] (Casado), [V] (Viúvo), [D] (Divorciado): ").upper().strip()
            if estado_civil in ['S', 'C', 'V', 'D']:
                usuario["Estado Civil"] = estado_civil
                break
            print("Erro: Estado civil inválido.")

        

        usuario["ID"] = identificador
        identificador+= 1
        dados_validos.append(usuario)

        
        sair = input("Deseja continuar? (S/N): ").upper().strip()
        if sair == 'N':
            break

    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exibe os dados cadastrados
print("\nUsuários cadastrados:")
for usuario in dados_validos:
    print(usuario)
