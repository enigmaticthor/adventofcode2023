from pathlib import Path
input_folder = Path("input")
input_file = input_folder / "day2.txt"
file = open(input_file,"r")
#total numbers of valid cubes
valid_criteria = {
    'red': 12,
    'green': 13,
    'blue': 14
}
games = {}
i = 0
for line in file:
    i += 1
    line = line.strip('Game ')
    line = line.strip('\n')
    if i < 10:
        number = line[:2]
        game = line[3:]
    elif i >= 10 and i < 100:
        number = line[:3]
        game = line[4:]
    else:
        number = line[:4]
        game = line[5:]
    game = game.strip(':').strip()
    game = game.split(';')
    sets = []
    for set in game:
        sets.append(set.strip().split(', '))
    number = number.strip(': ')
    games[number] = sets
file.close()
valid_games = []
invalid_games = []

def get_validity(color):
    valid = True
    color_split = color.split(' ')
    if "red" in color_split[1]:
        if int(color_split[0]) > 12:
            valid = False
    elif "green" in color_split[1]:
        if int(color_split[0]) > 13:
            valid = False
    elif "blue" in color_split[1]:
        if int(color_split[0]) > 14:
            valid = False
    return valid

def get_set_power(game_sets):
    set_value = ''
    return set_value

for game_id, game_sets in games.items():
    valid = True
    for pull in game_sets:
        if valid == False:
            break
        for color in pull:
            if valid == False:
                break
            valid = get_validity(color)
    if valid == True:
        valid_games.append(int(game_id))
    else:
        invalid_games.append(int(game_id))

print(sum(valid_games))