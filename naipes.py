import random
# A) ...
PALOS = '♠ ♡ ♢ ♣'.split(' ')
RANGO = '2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')
JUGADORES = 'Ana Bob Edu Jon'.split(' ')
# B) ...
mazo = [(p, r) for r in RANGO for p in PALOS]
# C) ...
random.shuffle(mazo)
# D) ...
reparte = (mazo[0::4], mazo[1::4], mazo[2::4], mazo[3::4])
# E) ...
manos = {n: h for n, h in zip(JUGADORES, reparte)}
# F) ...
for nombre, cartas in manos.items():
    print(f'{nombre}: {" ".join(f"{p+r:<3}" for (p, r) in cartas)}')
    print('-'*60)
# G) ...
primer_jugador = random.choice(JUGADORES)
# H) ...
primer_indice = JUGADORES.index(primer_jugador)
# I) ...
turnos = JUGADORES[primer_indice:] + JUGADORES[:primer_indice]
# J) ...
while manos[primer_jugador]:
    # K) ...
    for nombre in turnos:       # L) ...
        carta = random.choice(manos[nombre])
        manos[nombre].remove(carta)
        print(f'{nombre}: {carta[0] + carta[1]:<3} ', end='')
print()
