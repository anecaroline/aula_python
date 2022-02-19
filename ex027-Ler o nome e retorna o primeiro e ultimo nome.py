#lê um nome completo e retorna o primeiro e o ultimo nome.

nome = str(input()).strip()
nomeDividido = nome.split()
print("O primeiro nome é {}".format(nomeDividido[0]))
print("O ultimo nome é {}".format(nomeDividido[len(nomeDividido)-1]))