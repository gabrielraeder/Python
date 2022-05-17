from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


r = int(input('Em que ano você nasceu? '))
print(voto(r))
