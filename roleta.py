import random
import os

opcoes = ['🍇', '🍊', '🍎']
saldo = 20  # Saldo inicial


def limpar():
    print('\n' * 50)


print('\nMenu Principal\n')
print('1.Jogar Roleta')
print('2.Consultar Saldo')
print('3.Sair')


def jogo():
    global saldo

    while True:
        limpar()
        escolh_maquina = random.choices(opcoes, k=3)
        print('\nROLETA FRUTOSA')
        print('Seu objetivo é alcançar o combo de três frutas!\n')
        print(f'Saldo atual: {saldo},00 reais')
        if saldo < 2:
            print('Fim de jogo, saldo insuficiente.')
            break
        iniciar = input('Você gostaria de jogar?(sim/não): ').lower()
        if iniciar == 'sim':
            limpar()
            saldo -= 2  # Cobra a jogada
            print(
                f"\nResultado: {escolh_maquina[0]} | {escolh_maquina[1]} | {escolh_maquina[2]}\n")
            if len(set(escolh_maquina)) == 1:
                saldo += 10
                print(
                    f"🎉 TRINCA! Você ganhou 10 reais! Saldo atual: R${saldo},00")
                input('Pressione enter para retornar ao menu principal ')
            else:
                print(f'Você perdeu 2 reais, Saldo: R${saldo},00')
                input('Pressione enter para retornar ao menu principal ')
                break
        elif iniciar == 'não':
            print('Você saiu.')
            break


def consultar_saldo():
    limpar()
    print('Consultando saldo..\n')
    print(f'O seu saldo é de: R${saldo:.2f} reais.')
    input('Pressione enter para retornar ao menu ')


def interface():
    while True:
        limpar()
        print('\nMenu Principal\n')
        print('1.Jogar Roleta')
        print('2.Consultar Saldo')
        print('3.Sair')
        inicio = input('Selecione qual opção você deseja: ').lower().strip()
        if inicio == '1' or inicio == 'jogar roleta':
            if saldo >= 2:
                jogo()
            else:
                print('Você não possui saldo suficiente.')
        elif inicio == '2' or inicio == 'consultar saldo':
            consultar_saldo()
        elif inicio == '3' or inicio == 'sair':
            limpar()
            print('Você saiu.')
            break
        else:
            print('Selecione uma opção válida!')


interface()
