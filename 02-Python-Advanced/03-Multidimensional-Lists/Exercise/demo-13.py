dict = {
    'pres': '1 bar',
    'temp': '20 C',
    'duration': '100 cycles'
}


def t_shock(temp, duration):
    pass


def t_shock_v2(temp, duration, pres):
    pass


t_shock_v2(**dict)  # pass

print(*dict)  # pres temp duration
