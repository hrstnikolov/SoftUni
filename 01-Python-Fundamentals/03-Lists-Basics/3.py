# A-1 A-5 A-10 B-2

cards = input().split(' ')

team_a = []
team_b = []
for card in cards:
    player = int(card[card.index('-'):])

    if 'A' in card and player not in team_a:
        team_a.append(player)

    elif 'B' in card and player not in team_b:
        team_b.append(player)

players_a = 11 - len(team_a)
players_b = 11 - len(team_b)

print(f"Team A - {players_a}; Team B - {players_b}")

if players_a < 7 or players_b < 7:
    print('Game was terminated')

