from pathlib import Path
input_folder = Path("../input")
input_file = input_folder / "day2.txt"
file = open(input_file,"r")
games = {}
i = 0
for line in file:
    i += 1
    line = line.strip('Game ')
    line = line.strip('\n')
    if i < 10:
        number = line[:2]
        game = line[3:]
    elif i > 10 and i < 100:
        number = line[:3]
        game = line[4:]
    else:
        number = line[:4]
        game = line[5:]
    game = game.strip(': ')
    number = number.strip(': ')
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