file=open("./input/day2.txt","r")
games = {}
i = 0
for line in file:
    i += 1
    line = line.strip('Game ')
    line = line.strip('\n')
    if i < 10:
        number = line[:2]
        number = number.strip(': ')
        game = line[2:]
        game = game.strip()
    elif i > 10 and i < 100:
        number = line[:3]
        number = number.strip(': ')
        game = line[4:]
        game = game.strip(': ')
    else:
        number = line[:4]
        number = number.strip(': ')
        game = line[5:]
        game = game.strip()
    games[number] = game
file.close()
valid_games = []
#total numbers of valid cubes
valid_criteria = {
    'red': 12,
    'green': 13,
    'blue': 14
}
print(games)
