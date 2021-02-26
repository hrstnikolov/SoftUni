dict = {
    'pres': '1 bar',
    'temp': '20 C',
    'duration': '100 cycles'
}


def t_shock(temp, duration):
    pass


t_shock(**dict)  # TypeError: t_shock() got an unexpected keyword argument 'pres'