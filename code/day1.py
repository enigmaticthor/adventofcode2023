file=open("./input/day1.txt","r")
calibration = []
for line in file:
    line = line.strip('\n')
    calibration.append(line)
file.close()
text_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
def number_catcher(line):
    line_number_list = []
    line_characters = ''
    #take any numeric numbers and throw them in an array
    for x in line:
        if x.isnumeric():
            line_number_list.append(x)
            line_characters = ''
        else:
            #grab characters one at a time until there's a match, then remove all but the last character
            line_characters = line_characters + x
            for key, value in text_numbers.items():
                if key in line_characters:
                    line_number_list.append(value)
                    line_characters = line_characters[-1]
                    break
    return line_number_list
    

numbers = []
for line in calibration:
    line_numbers = number_catcher(line)
    line_number = line_numbers[0] + line_numbers[-1]
    numbers.append(int(line_number))
print(sum(numbers))
