
loop = 1

while loop <= 10:
    print(loop)
    loop += 1



chamada = 0

while chamada <= 9:
    chamada += 1
    if chamada == 5:
        print("pulando número 5")
        continue
    print(chamada)




nomes = input
while True:
    nome = nomes('digite um nome: ')
    if nome == 'sair':
        break
    print('Você digitou:', nome)




tentativa = 0
while tentativa < 3:
    senha = input("digite a senha: ")
    if senha == "1234":
        print("acesso permitido")
        break
    tentativa += 1
    if tentativa == 3:
        print("excedeu suas tentativas")
        break




contador = 1

while contador <= 19:

    contador +=1
    if contador %2 == 0:
        print(contador, " é par")
    continue
