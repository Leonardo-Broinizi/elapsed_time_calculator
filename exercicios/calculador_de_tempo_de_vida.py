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
data_atual = date.today()
natal = res = ''
ano_natal = mês_natal = dia_natal = anos = meses = dias = meses_totais = dias_totais = dia_mês = 0
níver = níver_hoje = mesversário = bissexto = False
# dias_meses = {'jan' : 31, 'fev' : 28, 'mar' : 31, 'abr' : 30, 'mai' : 31, 'jun' : 30, 'jul' : 31, 'ago' : 31, 'set' : 30, 'out' : 31, 'nov' : 30, 'dez' : 31}
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def cabeçalho():
    print(f'\033[1;34m{'-=-' * 15}')
    print(f'\033[31m{'> > > > \033[33mCALCULADOR DE TEMPO VIVIDO\033[31m < < < <':^45}')
    print(f'\033[34m{'-=-' * 15}\n')

def recebe_valida_data(bissexto): # Nesta função, como o nome diz, eu recebo e valido a data de nascimento da pessoa.
    while True:
        while True:
            natal = str(input('\033[m\033[1mDigite o dia do seu nascimento no formato [dd/mm/aaaa]: ')).strip().replace(
                '/', '')
            if len(natal) != 8:
                print('ERRO! O formato inserido não corresponde ao exigido [dd/mm/aaaa]. Por favor, tente novamente.')
            else:
                break
        ano_natal = int(natal[-4:])
        mês_natal = int(natal[2:4])
        dia_natal = int(natal[:2])
        if ano_natal % 4 == 0 and ano_natal % 100 != 0:  # Verificador do ano bissexto:
            bissexto = True
        elif ano_natal % 400 == 0:
            bissexto = True
        else:
            bissexto = False
        if ano_natal > ano:
            print(f'ERRO! O ano informado não pode ser maior que o ano atual ({ano}). Por favor, tente novamente.')
        elif mês_natal > 12:
            print('ERRO! O mês informado não pode ser maior que 12. Por favor, tente novamente.')
        elif dia_natal > 31:
            print('ERRO! O dia informado não pode ser maior do que 31. Por favor, tente novamente.')
        elif ano_natal == ano and mês_natal > mês or ano_natal == ano and mês_natal == mês and dia_natal > dia:
            print(f'ERRO! A data informada não pode ser maior que a data atual ({data_atual}). Por favor, tente novamente.')
        elif dia_natal > 30 and str(mês_natal) in '469' or mês_natal == 11 and dia_natal > 30:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 30. Por favor, tente novamente.')
        elif mês_natal == 2 and bissexto and dia_natal > 29:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 29. Por favor, tente novamente.')
        elif mês_natal == 2 and dia_natal > 28 and not bissexto:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 28. Por favor, tente novamente.')
        else:
            return dia_natal, mês_natal, ano_natal, bissexto
            break

def verifica_níver(níver, níver_hoje, mesversário):
    if int(mês_natal) < mês: # Verificador se já fez aniversário este ano:
        níver = True
    elif int(mês_natal) == mês and int(dia_natal) < dia:
        níver = True
    elif int(mês_natal) == mês and int(dia_natal) == dia:
        níver_hoje = True
    if int(dia_natal) < dia:
        mesversário = True
    return níver, níver_hoje, mesversário

def contador(dias):

    if níver_hoje:
        anos = ano - int(ano_natal)
        meses = 0 # linha desnecessária mas preferi deixar explícito, até pra me situar
        dias = 0
    elif níver:
        anos = ano - int(ano_natal)
        meses = mês - int(mês_natal)
        for d_m in range(dias_meses[int(mês_natal)], dias_meses[mês]):
            dias += d_m
        dias -= int(dia_natal) - (dias_meses[mês] - dia)
    else:
        anos = ano - int(ano_natal) - 1

    print(f'anos: {anos}, meses: {meses}, dias: {dias} ')
    return dias, meses, anos, dias_totais, meses_totais


ano = data_atual.year # Nessas linhas atribuo o ano, mês e dia a variáveis com esses respectivos nomes.
mês = data_atual.month
dia = data_atual.day

if dia > 9 and mês > 9:  # Nesse bloco eu formato a variável 'data_atual' para ser uma string no formado dd/mm/aaaa (colocando o zero na casa da dezena, caso ela esteja vazia).
    data_atual = str(f'{dia}/{mês}/{ano}')
elif dia < 9 and mês > 9:
    data_atual = str(f'0{dia}/{mês}/{ano}')
elif dia > 9 and mês < 9:
    data_atual = str(f'{dia}/0{mês}/{ano}')
else:
    data_atual = str(f'0{dia}/0{mês}/{ano}')

while True:
    cabeçalho()
    natal_tupla = recebe_valida_data(bissexto) # ano_natal, mês_natal, dia_natal
    dia_natal = str(natal_tupla[0]) if natal_tupla[0] > 9 else str(f'0{natal_tupla[0]}')
    mês_natal = str(natal_tupla[1]) if natal_tupla[1] > 9 else str(f'0{natal_tupla[1]}')
    ano_natal = str(natal_tupla[2])
    bissexto = natal_tupla[3]


    aniversário = verifica_níver(níver, níver_hoje, mesversário)
    níver = aniversário[0]
    níver_hoje = aniversário[1]
    mesversário = aniversário[2]


    if níver_hoje:
        print('Parabéns, você está fazendo aniversário hoje!')

    tempo = contador(dias)
    print(tempo)
    while True:
        res = str(input('Quer verificar a contagem de tempo de vida de mais alguém? [S/N] ')).strip().upper()
        if res in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if res == 'N':
        break














'''data = data_atual.strftime('%d/%m/%Y')# Se o 'y' estiver minúsculo só irá retornar os últimos dois digitos do ano atual.
print(f'\033[1;34m{'-=-' * 15}')
print(f'\033[31m{'> > > > \033[33mCALCULADOR DE TEMPO VIVIDO\033[31m < < < <':^45}')
print(f'\033[34m{'-=-' * 15}\n')
while True:
    níver = str(input('\033[m\033[1mDigite a data do seu aniversário [dd/mm/aaaa]: ')).strip()
    níver = níver.replace('/','') # percebí que essa linha pareceu desnecessária. Vejamos...
    if len(níver) != 8 or int(níver) <= 99999:
        print('ERRO! O valor informado não corresponde ao formado exigido [dd/mm/aaaa].\nPor favor, tente novamente.')
    elif int(níver[:2]) > int(data_atual.day) and int(níver[2:4]) > int(data_atual.month) and int(níver[-4:]) > int(data_atual.year):
        print('ERRO! Os valores informados são superiores ao número de dias, mês e ano atual.')
    elif int(níver[-4:]) > int(data_atual.year):
        print(f'ERRO! O ano informado não pode ser superior ao ano atual ({data_atual.year})')
    else:
        break
if int(data_atual.month) < int(níver[2:4]) or int(data_atual.month) == int(níver[2:4]) and int(data_atual.day) < int(níver[:2]):
    print('Ainda não fez aniversário esse ano!')
elif int(data_atual.month) == int(níver[2:4]) and int(data_atual.day) == int(níver[:2]):
    print('Fazendo aniversário hoje!')
else:
    print('Já fez aniversário!')

anos = int(data_atual.year) - int(níver[-4:])
meses = int(data_atual.month) - int(níver[2:4])
dias = int(data_atual.day) - int(níver[:2])
aniversário = False
print(anos, meses, dias)'''