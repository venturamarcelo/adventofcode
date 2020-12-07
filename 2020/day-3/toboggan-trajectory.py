# Reading file and creating map
inputfile = open("input.txt").read()
problem_map = []
for row in inputfile.split("\n"):
    problem_map.append([pos for pos in row])
# Part 1 - Searching for '#' 1,3
def traverse(map,  step_down, step_right):
    tree_count=0
    row=0
    col=0
    while (row < len(map)):
        if map[row][col%len(map[0])] == '#':
            tree_count += 1
        row += step_down
        col += step_right
    return tree_count
D1R3=traverse(problem_map,1,3)
print(D1R3)
# Part 2 
D1R1=traverse(problem_map,1,1)
print(D1R1)
D1R5=traverse(problem_map,1,5)
print(D1R5)
D1R7=traverse(problem_map,1,7)
print(D1R7)
D2R1=traverse(problem_map,2,1)
print(D2R1)

print(D1R1*D1R3*D1R5*D1R7*D2R1)