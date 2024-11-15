from random import randint

continuar = True
while continuar == True:
    # GERA OS PRIMEIROS 9 NÚMEROS
    n1 = randint(0,9)
    n2 = randint(0,9)
    n3 = randint(0,9)
    n4 = randint(0,9)
    n5 = randint(0,9)
    n6 = randint(0,9)
    n7 = randint(0,9)
    n8 = randint(0,9)
    n9 = randint(0,9)

    cpf = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

    # GERAÇÃO VALIDA DO 1º DIGITO VERIFICADOR
    digito1 = (n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2) * 10 % 11
    if digito1 == 10:
        digito1 = 0
    cpf.append(digito1)


    # GERAÇAO VALIDA DO 2º DIGITO VERIFICADOR
    digito2 = (n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + digito1*2) * 10 % 11
    if digito2 == 10:
        digito2 = 0
    cpf.append(digito2)


    # CPF SEM PONTUAÇÃO
    for numero in cpf:
        print(numero, end="")

    print('')

    escolha = input('Gerar novamente? (s/n) ')
    if escolha == 's':
        continuar = True
    elif escolha == 'n':
        continuar = False