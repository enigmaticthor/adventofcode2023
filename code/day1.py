file=open("./input/day1.txt","r")
calibration = []
for line in file:
    line = line.strip('\n')
    calibration.append(line)
file.close()
print(calibration)
#for line in calibration:
    #for x in line:
