##leia o nome completo de uma pessoa

nome = str(input()).strip()
##strip tira os espacos iniciais e finais dados pelo usuario
##o nome com todas as letras minusculas
print("Seu nome com lestras maiusculas é:",nome.upper())
##print("Seu nome com lestras maiusculas é:" .format(nome.upper())
print("Seu nome com lestras minusculas é:",nome.lower())
##print("Seu nome com lestras minuscula é:" .format(nome.lower())
##quantas letras ao todo sem contar espaços
##ou
##print("O seu nome possui {} letras: ".format(len(nome) - nome.count(" ")))
nomeSemEspaco = len(nome.replace(" ",""))
print("O seu nome possui {} letras: ".format(nomeSemEspaco))
##quantas letras tem o primeiro nome
nomeDividido = nome.split()
print("Seu primeiro nome tem {} letras:".format(len(nomeDividido[0])))
##ou
##print("Seu primeiro nome tem {} letras:".format(nome.find(" ")))
