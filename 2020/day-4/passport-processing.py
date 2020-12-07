import re
def fields_valid(passport):
    expected_eye_color = ['amb','blu','brn','gry','grn','hzl','oth']
    if not 1920 <= int(passport['byr']) <= 2002: return False
    if not 2010 <= int(passport['iyr']) <= 2020: return False
    if not 2020 <= int(passport['eyr']) <= 2030: return False
    if not re.compile('#[0-9a-f]{6}').match(passport['hcl']): return False
    if not re.compile("[0-9]{9}(?![0-9])").match(passport['pid']): return False
    if passport['ecl'] not in expected_eye_color: return False
    if not re.compile('[0-9]+(cm|in)').match(passport['hgt']): return False
    else: 
        if 'cm' in passport['hgt'] and 150 <= int(passport['hgt'][:-2]) <= 193:
            pass
        else: 
            if 'in' in passport['hgt'] and 59 <= int(passport['hgt'][:-2]) <= 76:
                pass
            else: return False
    return True

def fields_present(passport):
    expected_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for field in expected_fields:
        if field not in passport:
            return False
    return True

def read_passport(i: int, passport: dict):
    if inputfile[i] in (None, "\n"):
        return passport
    else:
        for entry in inputfile[i].split(' '):
            field = {entry.split(':')[0] : entry.split(':')[1].rstrip("\n")}
            passport.update(field)
        return read_passport(i+1, passport)

# Reading input file
inputfile = open(file="input2.txt", mode="r").readlines()

i = 0
y = 0
passport_list = []
while y < len(inputfile):
    if inputfile[y] in (None, "\n"):
        # print(f"{i} - {y}")
        passport_list.append(read_passport(i,{}))
        y+=1
        i = y
    else: 
        y+=1

# Checking fields
result = 0
for passport in passport_list:
    if fields_present(passport) and fields_valid(passport):
        result+=1
print(result)