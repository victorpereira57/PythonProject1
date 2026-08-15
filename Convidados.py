convidados = []

while True:
    nome = input("Digite o nome do convidado (ou 'fim' para encerrar o programa)")
    if nome == "fim":
        break

    convidados.append(nome)

print("Lista de convidados: ", convidados)
print(f"Quantidade de convidados: {len(convidados)}")

