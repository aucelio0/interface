# importar do arquivo
from modulo import *

# biblioteca
import os

if __name__ == "__main__":
    cc = ContaCorrente('','', '1001-1', '10010-1', 0)

    # entrada de dados
    cc.nome = input('Informe o nome do titular: ').capitalize()
    cc.cpf= input('Informe o cpf do titular: ')

while True: 

    # saída de dados
    print(F'\n{'-'*20} DADOS {'-'*20}')
    print(f'\nNome do titular: {cc.nome}.')
    print(f'CPF do titular: {cc.cpf}.')
    print(f'Conta: {cc.conta}.')
    print(f'Agência: {cc.agencia}.')
    print(f'Saldo: R$ {cc.saldo}.\n')

    print(f'\n{cc.nome} dejesa realizar qual operação?')
    print('1 - Consulltar saldo')
    print('2 - Realizar depósito.')
    print('3 - Realizar saque.')
    print('4 - Sair do programa.')

    opcao = input('Informe sua opção: ')
    os.system('cls')
    
    match opcao:
        case '1':
            print('Consultar saldo\n')
            print(f'Saldo disponível: R$ {cc.consultar_saldo():,.2f}.')
            continue
        case '2':
            valor = float(input('Valor do depósito: R$ ').replace(',','.'))
            if valor > 0:
                cc.saldo = cc.fazer_deposito(valor)
                print('Depósito efetuado com sucesso.')
                print(f'Saldo atual: R$ {cc.consultar_saldo():,.2f}.')
            else:
             print('Valor inválido')
            continue
        case '3':
                valor = float(input('Valor do saque: R$ ').replace(',','.'))
                if valor <= cc.saldo: 
                    cc.saldo = cc.fazer_saque(valor)
                    print('Saque efetuado com sucesso.')
                    print(f'Saldo atual: R$ {cc.consultar_saldo():,.2f}.')
                else:
                    print('Não foi possível efetuar saque.')
                    continue
        case '4':
            print('Programa encerrado!')
            break
        case _:
            print('Opção inválida!')
            continue

    




    