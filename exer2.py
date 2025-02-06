usuario = []

while True:
    

    nome = input("Digite seu nome: ").lower().strip()
    senha = input("Digite sua senha:").lower().strip()

    if senha == nome:
        continue
    else:
        usuario.append(nome)
        usuario.append(senha)
        break

print(f"usuario 1: {usuario}")