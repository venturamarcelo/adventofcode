inputfile = open(file="input.csv", mode="r") 
Lines = inputfile.readlines()
# part 1 and 2
countPart1 = 0
countPart2 = 0
for line in Lines:
    policy = line.split(':')[0].rstrip()                            # Get the policy         i.e. '1-3 a'
    password = line.split(':')[1].rstrip()                          # Get the password       i.e. 'abcada'
    char = policy.split()[1]                                        # Get the character      i.e. 'a'
    maxChar = int(policy.split()[0].split("-")[1])                  # Get the max            i.e. '3'
    minChar = int(policy.split()[0].split("-")[0])                  # Get the min            i.e. '11
    valid1 = minChar <= password.count(char) <= maxChar
    valid2 = (password[minChar] == char) ^ (password[maxChar] == char)
    print(f"policy: {policy}, pass:{password}, char: {char}, min: {minChar}, max: {maxChar}, count: {password.count(char)}, valid1: {valid1}, valid2: {valid2}")
    if valid1: countPart1 = countPart1 + 1
    if valid2: countPart2 = countPart2 + 1
print(f"RESULT= part1: {countPart1} , part2: {countPart2}")
