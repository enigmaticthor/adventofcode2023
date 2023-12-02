file=open("./input/day1.txt","r")
calibration = []
for line in file:
    line = line.strip('\n')
    calibration.append(line)
file.close()

def number_catcher(test):
    return test.isnumeric()

numbers = []
for line in calibration:
    line_numbers = []
    for x in line:
        if x.isnumeric():
            line_numbers.append(x)
    line_number = line_numbers[0] + line_numbers[-1]
    numbers.append(int(line_number))
print(sum(numbers))