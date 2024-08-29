from datetime import date
if date.today().day > 9 and date.today().month > 9:
    data_em_texto = (f'{date.today().day}/{date.today().month}/{date.today().year}')
elif date.today().day > 9:
    data_em_texto = (f'{date.today().day}/0{date.today().month}/{date.today().year}')
elif date.today().month > 9:
    data_em_texto = (f'0{date.today().day}/{date.today().month}/{date.today().year}')
else:
    (f'0{date.today().day}/0{date.today().month}/{date.today().year}')
print(data_em_texto)
