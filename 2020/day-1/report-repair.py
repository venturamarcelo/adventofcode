inputfile = open(file="input.csv", mode="r") 
Lines = inputfile.readlines()
# part 1
for i, a in enumerate(Lines):
    for b in Lines[i:]:
        #print(f"Checking {int(a)} + {int(b)} = {int(a)+int(b)}")
        if int(a) + int(b) == 2020:
            print(f"AHA! {int(a)} + {int(b)} = 2020 - Answer is: {int(a)*int(b)}")
            break
# part 2
for i, a in enumerate(Lines):
    shortList = Lines[i:]
    for y, b in enumerate(shortList):
        shorterList = shortList[y:]
        for c in shorterList:
            if int(a) + int(b) + int(c) == 2020:
                answer = int(a) * int(b) * int(c)
                print(f"WOHOO! {int(a)} + {int(b)} + {int(c)} = 2020 - Answer is: {answer}")