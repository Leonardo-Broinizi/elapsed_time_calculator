#    Quis fazer um verificador que calcule o tempo corretamente, levando em consideração os anos bissextos,
# incluindo o cálculo para anos bissextos longínquos, mesmo que nenhuma pessoa viva tenha passados por tal época.
# Quero que a calculadora sirva para calcular com precisão o tempo decorrido de qualquer data (de alguns milênios)
# até a atual do usurário, caso alguém queira calcular a data de um personagem ou evento histórico.
# Mesmo assim, mantive o tom da interação pessoal, dando parabéns caso a data coincida com o aniversário.
# Pode parecer ser um pouco contraditório, mas escolhi fazer assim. De qualquer forma, com alguns ajustes
# esse código pode virar um calculador de tempo decorrido explicitamente mais genérico, com o usuário declarando
# a data inicial e a final. Talvez eu faça isso em breve...


''' Preciso verificar se essa a conta está correta (dos dias, meses e anos decorridos em quem já fez aniversário).
Ainda falta: calcular esses mesmos parâmetros para quem ainda não fez aniversário,
calcular o tempo decorrido em mêses e em dias (e, quem sabe, em semanas e etc).
Validar se o tempo foi superior a zero. Quem sabe aceitar outros formatos, como d/m/aa.'''

from datetime import date


def cabeçalho():
    print(f'\033[1;34m{'-=-' * 15}')
    print(f'\033[31m{'> > > > \033[33mCALCULADOR DE TEMPO VIVIDO\033[31m < < < <':^45}')
    print(f'\033[34m{'-=-' * 15}\n')


def recebe_valida_data(ano_atual, mes_atual,
                       dia_atual):  # Nesta função, como o nome diz, eu recebo e valido a data de nascimento da pessoa.
    while True:
        while True:
            natal = str(input('\033[m\033[1mDigite o dia do seu nascimento no formato [dd/mm/aaaa]: ')).strip().replace(
                '/', '')
            if len(natal) != 8:
                print('ERRO! O formato inserido não corresponde ao exigido [dd/mm/aaaa]. Por favor, tente novamente.')
            else:
                break
        ano_nasc = int(natal[-4:])
        mes_nasc = int(natal[2:4])
        dia_nasc = int(natal[:2])

        bissexto = False
        if ano_nasc % 4 == 0 and ano_nasc % 100 != 0:
            bissexto = True
        elif ano_nasc % 400 == 0:
            bissexto = True

        meses_30_dias = [4, 6, 9, 11]

        if ano_nasc > ano_atual:
            print(
                f'ERRO! O ano informado não pode ser maior que o ano atual ({ano_atual}). Por favor, tente novamente.')
        elif ano_nasc == ano_atual and mes_nasc > mes_atual:
            print(f'ERRO! A data informada não pode ser maior que a data atual. Por favor, tente novamente.')
        elif ano_nasc == ano_atual and mes_nasc == mes_atual and dia_nasc > dia_atual:
            print(f'ERRO! A data informada não pode ser maior que a data atual. Por favor, tente novamente.')
        elif mes_nasc < 1 or mes_nasc > 12:
            print('ERRO! Mês inválido. Por favor, tente novamente.')
        elif dia_nasc < 1 or dia_nasc > 31:
            print('ERRO! Dia inválido. Por favor, tente novamente.')
        elif mes_nasc in meses_30_dias and dia_nasc > 30:
            print(f'ERRO! O mês {mes_nasc} não pode ter mais de 30 dias. Por favor, tente novamente.')
        elif mes_nasc == 2:
            if bissexto and dia_nasc > 29:
                print('ERRO! Em ano bissexto, Fevereiro não pode ter mais de 29 dias. Por favor, tente novamente.')
            elif not bissexto and dia_nasc > 28:
                print('ERRO! Para o ano informado, Fevereiro não pode ter mais de 28 dias. Por favor, tente novamente.')
        else:
            return dia_nasc, mes_nasc, ano_nasc


def calcular_tempo_vivido(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    dias_meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    ano_calc = ano_atual
    mes_calc = mes_atual
    dia_calc = dia_atual

    if dia_calc < dia_nasc:
        mes_calc -= 1
        mes_anterior = mes_calc
        if mes_anterior == 0:  # Caso empreste de Janeiro, o mês anterior é Dezembro do ano anterior
            mes_anterior = 12

        # Verifica se o ano do qual estamos pegando o mês é bissexto para ajustar Fevereiro
        ano_do_mes_anterior = ano_calc if mes_calc > 0 else ano_calc - 1
        if mes_anterior == 2:
            if ano_do_mes_anterior % 4 == 0 and (ano_do_mes_anterior % 100 != 0 or ano_do_mes_anterior % 400 == 0):
                dia_calc += 29
            else:
                dia_calc += 28
        else:
            dia_calc += dias_meses[mes_anterior]

    if mes_calc < mes_nasc:
        ano_calc -= 1
        mes_calc += 12

    anos = ano_calc - ano_nasc
    meses = mes_calc - mes_nasc
    dias = dia_calc - dia_nasc

    return anos, meses, dias


while True:
    cabeçalho()
    data_atual = date.today()

    dia_nasc, mes_nasc, ano_nasc = recebe_valida_data(data_atual.year, data_atual.month, data_atual.day)

    if dia_nasc == data_atual.day and mes_nasc == data_atual.month:
        if ano_nasc == data_atual.year:
            print('\n\033[1;32mBem-vindo(a) ao mundo! Você nasceu hoje!\033[m')
        else:
            idade = data_atual.year - ano_nasc
            print(f'\n\033[1;32mFeliz aniversário! Parabéns pelos seus {idade} anos!\033[m')

    anos, meses, dias = calcular_tempo_vivido(dia_nasc, mes_nasc, ano_nasc, data_atual.day, data_atual.month,
                                              data_atual.year)

    print('\n\033[1mAté hoje, você viveu:')
    if anos > 0:
        print(f'\033[1;36m{anos} ano(s)')
    if meses > 0:
        print(f'{meses} mes(es)')
    if dias > 0:
        print(f'{dias} dia(s)\033[m')
    if anos == 0 and meses == 0 and dias == 0 and ano_nasc != data_atual.year:
        # Caso especial para aniversário, já que a mensagem de parabéns apareceu acima
        print(f'\033[1;36mExatamente {data_atual.year - ano_nasc} ano(s)\033[m')
    elif anos == 0 and meses == 0 and dias == 0 and ano_nasc == data_atual.year:
        pass  # Não imprime nada se a pessoa nasceu hoje

    while True:
        res = str(input('\n\033[1mQuer verificar a contagem de tempo de vida de mais alguém? [S/N] ')).strip().upper()
        if res not in 'SN' or res == '':
            print('\033[31mERRO! Responda apenas S ou N.\033[m')
        else:
            break
    if res == 'N':
        print('\n\033[1;34mAté mais!\033[m')
        break
    print()