import random  # Para gerar itens aleatóriamente
import os  # Para interagir com o sistema operacional
import unicodedata  # Para palavras com acentuação
import pyfiglet  # Para fontes personalizadas, é necessária a instalação por pip


def remover_acentos(texto):
    # Função responsável por remover acentos em textos definidos
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


opcoes = ['🍇', '🍊', '🍎']  # Opções para o jogo da roleta
saldo = 20  # Saldo inicial


def limpar():
    print('\n' * 50)


# Opções para o jogo do Caça Níquel
simbolos = ['🍒', '🍋', '🔔', '⭐', '💎', '7️⃣']
pesos = [30,   25,   20,   15,   7,    3]  # Peso de cada opção

multiplicadores = {
    ('🍒', '🍒', '🍒'): (2,  'TRINCA DE CEREJAS!'),
    ('🍋', '🍋', '🍋'): (3,  'TRINCA DE LIMÕES!'),
    ('🔔', '🔔', '🔔'): (5,  'TRINCA DE SINOS!'),
    ('⭐', '⭐', '⭐'): (8,  'TRINCA DE ESTRELAS!'),
    ('💎', '💎', '💎'): (15, 'TRINCA DE DIAMANTES!'),
    ('7️⃣', '7️⃣', '7️⃣'): (50, '🎰 JACKPOT! TRÊS SETES!'),
}


def caca_niquel():
    # Função responsável pelo jogo Caça Níquel
    global saldo

    while True:
        limpar()
        print('\nCAÇA-NÍQUEL')
        print('Combine três símbolos iguais para ganhar!\n')  # Menu principal
        print(f'Saldo atual: R${saldo},00')

        if saldo < 10:
            print('Saldo insuficiente para jogar (mínimo R$10,00).')
            # Processamento
            input('Pressione enter para retornar ao menu principal ')
            break

        try:
            aposta = int(
                input('Quanto deseja apostar? (mínimo 10, máximo 500): R$'))
        except ValueError:
            print('Valor inválido.')
            continue

        if aposta < 10 or aposta > 500:
            print('Aposta fora do intervalo permitido.')
            continue
        if aposta > saldo:
            print('Você não tem saldo suficiente para essa aposta.')
            continue

        iniciar = input('Confirmar aposta e girar? (sim/não): ').lower()
        if iniciar == 'nao':
            print('Você saiu.')
            break
        elif iniciar != 'sim':
            continue

        limpar()
        saldo -= aposta

        rolos = tuple(random.choices(simbolos, weights=pesos, k=3))
        print(f'\nResultado: {rolos[0]} | {rolos[1]} | {rolos[2]}\n')

        if rolos in multiplicadores:
            mult, mensagem = multiplicadores[rolos]
            premio = aposta * mult
            saldo += premio
            print(f'🎉 {mensagem}')
            print(f'Você ganhou R${premio},00! (x{mult})')
            print(f'Saldo atual: R${saldo},00')
        else:
            print(f'Que pena! Você perdeu R${aposta},00.')
            print(f'Saldo atual: R${saldo},00')

        input('\nPressione enter para retornar ao menu principal ')
        break


def roleta():
    # Função responsável pelo jogo da roleta
    global saldo

    while True:
        limpar()
        escolh_maquina = random.choices(opcoes, k=3)
        print('\nROLETA FRUTOSA')
        # Menu Principal
        print('Seu objetivo é alcançar o combo de três frutas!\n')
        print(f'Saldo atual: {saldo},00 reais')
        print('Obs: Cada jogada custa um total de 10 reais.')
        if saldo < 2:
            print('Fim de jogo, saldo insuficiente.')
            break
        iniciar = input('Você gostaria de jogar? (sim/não): ').lower()

        if iniciar == 'sim':
            limpar()
            saldo -= 2  # Cobra a jogada
            print(
                f"\nResultado: {escolh_maquina[0]} | {escolh_maquina[1]} | {escolh_maquina[2]}\n")
            if len(set(escolh_maquina)) == 1:
                saldo += 10
                print(
                    # Ganho
                    f"🎉 TRINCA! Você ganhou 10 reais! Saldo atual: R${saldo},00")
                input('Pressione enter para retornar ao menu principal ')
            else:
                print(f'Você perdeu 2 reais, Saldo: R${saldo},00')  # Perda
                input('Pressione enter para retornar ao menu principal ')
                break
        elif iniciar == 'nao':  # Opção
            print('Você saiu.')
            input('Pressione enter para retornar ao menu principal ')
            break
        else:
            print('Opção inválida! Digite sim ou não.')  # Entrada Inválida
            input('Presione enter para tentar novamente ')
            continue


def consultar_saldo():
    # Função responsável por consultar saldo do usuário
    global saldo
    limpar()
    print('Consultando saldo..\n')
    print(f'O seu saldo é de: R${saldo:.2f} reais.\n')
    print('1. Adicionar saldo')
    print('-----------')  # Menu Principal
    print('2. Sacar saldo')
    print('-----------')
    print('3. Retornar ao menu\n')
    escolha_saldo = input(
        'Selecione qual opção você deseja: ').lower().strip()
    if escolha_saldo == '1' or escolha_saldo == 'adicionar saldo':  # Adiciona saldo
        try:
            limpar()
            deposito = float(
                input('Insira a quantidade que deseja depositar: R$'))
            if deposito <= 0:
                print('O valor deve ser maior que zero.')
                input('Pressione enter para retornar ao menu principal ')
            else:
                saldo += deposito
                print(f'Você depositou R${deposito:.2f} reais')
                print(f'Seu novo saldo: R${saldo:.2f} reais')
                input('Pressione enter para retornar ao menu principal')
        except ValueError:
            print('Valor inválido, insira apenas números.')
    elif escolha_saldo == '2' or escolha_saldo == 'sacar saldo':  # Saca Saldo
        try:
            limpar()
            print(f'\nSeu saldo atual é de: R${saldo} reais\n')
            saque = float(input('Digite o valor que gostaria de sacar: R$'))
            if saque > saldo:
                print('Você não possui saldo suficiente para saque.')
                input('Pressione enter para retornar ao menu principal ')
            elif saque <= saldo:
                saldo -= saque
                print(f'\nVocê sacou um valor de R${saque:.2f} reais')
                print(f'Seu novo saldo: R${saldo:.2f} reais\n')
                input('Pressione enter para retornar ao menu principal ')
        except ValueError:
            print('Valor inválido, insira apenas números')
    elif escolha_saldo == '3' or escolha_saldo == 'retornar ao menu':  # Retorna ao menu principal
        limpar()
        main()


def interface():
    # Função responsável por mostrar a interface
    while True:
        limpar()
        print(pyfiglet.figlet_format('Cassino', font='slant'))
        print('\nMenu Principal\n')
        print('1. Jogar Roleta')
        print('2. Jogar Caça níquel')  # Menu Principal
        print('3. Consultar Saldo')
        print('4. Sair')
        inicio = input('Selecione qual opção você deseja: ').lower().strip()
        if inicio == '1' or inicio == 'jogar roleta':  # Opção que entra no jogo da roleta
            if saldo >= 2:
                roleta()
            else:
                print('Você não possui saldo suficiente.')
        elif inicio == '2' or inicio == 'jogar caca niquel':  # Opção que entra no jogo do Caça Níquel
            caca_niquel()
        elif inicio == '3' or inicio == 'consultar saldo':  # Opção que entra para consulta de saldo
            consultar_saldo()
        elif inicio == '4' or inicio == 'sair':  # Opção que sai do programa
            limpar()
            print('Você saiu.')
            break
        else:
            print('Selecione uma opção válida!')


def main():
    # Função main para chamar o programa
    while True:
        interface()
        limpar()
        decisao = input(
            'Deseja realmente sair? (sim/não): ').lower().strip()
        if decisao == 'sim':
            limpar()
            print('Obrigado por jogar! Até logo.')
            break
        if decisao == 'nao':
            continue
        else:
            print('Opção inválida, voltando ao menu principal...')
            continue


main()
