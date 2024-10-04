#    Salvei aqui o seguinte trecho bagunçado de código para me lembrar de que é possível
# fazer uma atribuição a uma variável com uma strint formatada, como nas linhas 10 a 12.

'''from datetime import date
from random import randint
ano = date.today().year
mês = date.today().month
data_atual = date.today()
sor = 0
sorteio_a = '{}/{}/{}/{}/{}'.format(randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5))
sorteio_b = (f'{randint(1,5)}+{randint(1,5)}++{randint(1,5)}+-+{randint(1,5)}--{randint(1,5)}-{randint(1,5)}')
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)
print(sorteio_a)
print(sorteio_b)'''

#    Código para pegar a data atual no padrão brasileiro (dd/mm/aa ou dd/mm/aaaa):
#   Com o método srtftime:

'''from datetime import date
data_atual = date.today()
data = data_atual.strftime('%d/%m/%Y')# Se o 'y' estiver minúsculo só irá retornar os últimos dois digitos do ano atual.
print(data)

#    De maneira muito mais trabalhosa sem o método srtftime:

from datetime import date
if date.today().day > 9 and date.today().month > 9:
    data_em_texto = (f'{date.today().day}/{date.today().month}/{date.today().year}')
elif date.today().day > 9:
    data_em_texto = (f'{date.today().day}/0{date.today().month}/{date.today().year}')
elif date.today().month > 9:
    data_em_texto = (f'0{date.today().day}/{date.today().month}/{date.today().year}')
else:
    (f'0{date.today().day}/0{date.today().month}/{date.today().year}')
print(data_em_texto)'''

def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print('Media: ', calcular_media(10, 20, 30))

quadrado = lambda x: x ** 2
print('Olá, mundo!')
print(quadrado(5))

