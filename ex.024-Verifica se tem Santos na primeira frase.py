nomeCidade = str(input()).strip()
nomeDividido = nomeCidade.upper().split(" ")
print(nomeDividido)

print("SANTO" in nomeDividido[0])

##nomeDividido[:5] caracteres da palavra Santos. as vezes não precisa usar o in e nem usar o split
nomeCidade = str(input()).strip().upper()
print("SANTO" in nomeCidade[:5])

