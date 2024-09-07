from datetime import date
data_atual = date.today()
natal = ''
ano_natal = mês_natal = dia_natal = 0
níver = níver_hoje = False

def cabeçalho():
    print(f'\033[1;34m{'-=-' * 15}')
    print(f'\033[31m{'> > > > \033[33mCALCULADOR DE TEMPO VIVIDO\033[31m < < < <':^45}')
    print(f'\033[34m{'-=-' * 15}\n')

def recebe_valida_data(): # Nesta função, como o nome diz, eu recebo e valido a data de nascimento da pessoa.
    while True:
        bissexto = False
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
        if ano_natal > ano:
            print(f'ERRO! O ano informado não pode ser maior que o ano atual ({ano}). Por favor, tente novamente.')
        elif mês_natal > 12:
            print('ERRO! O mês informado não pode ser maior que 12. Por favor, tente novamente.')
        elif dia_natal > 31:
            print('ERRO! O dia informado não pode ser maior do que 31. Por favor, tente novamente.')
        elif ano_natal == ano and mês_natal > mês or ano_natal == ano and mês_natal == mês and dia_natal > dia:
            print(
                f'ERRO! A data informada não pode ser maior que a data atual ({data_atual}). Por favor, tente novamente.')
        elif dia_natal > 30 and str(mês_natal) in '469' or mês_natal == 11 and dia_natal > 30:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 30. Por favor, tente novamente.')
        elif mês_natal == 2 and bissexto and dia_natal > 29:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 29. Por favor, tente novamente.')
        elif mês_natal == 2 and dia_natal > 28 and not bissexto:
            print('ERRO! Para o mês informado o valor do dia não pode ser superior a 28. Por favor, tente novamente.')
        else:
            print(f'Ano_natal: {ano_natal}\nMês_natal: {mês_natal}\nDia_natal: {dia_natal}')
            return dia_natal, mês_natal, ano_natal
            break

def verifica_níver(níver, níver_hoje):
    if mês_natal < mês: # Verificador se já fez aniversário este ano:
        níver = True
        print(mês, mês_natal)
        print('Níver pelo mês')
    elif mês_natal == mês and dia_natal < dia:
        níver = True
        print('Níver pelo dia')
    elif mês_natal == mês and dia_natal == dia:
        níver_hoje = True


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


cabeçalho()
natal_tupla = recebe_valida_data() # ano_natal, mês_natal, dia_natal
print(f'Natal_lista: {natal_tupla}, Type: {type(natal_tupla)}')
dia_natal = str(natal_tupla[0]) if natal_tupla[0] > 9 else str(f'0{natal_tupla[0]}')
print(dia_natal, type(dia_natal))
verifica_níver(níver, níver_hoje)
if níver:
    print('Você já fez aniversário!')
elif níver_hoje:
    print('Parabéns, você está fazendo aniversário hoje!')






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