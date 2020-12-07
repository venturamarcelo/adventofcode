import bisect
def search(i, range_start, range_end, boarding_pass):
    # print(boarding_pass)
    if range_start == range_end: return range_start
    mid = (range_start+range_end)//2
    if boarding_pass[i] == 'F' or boarding_pass[i] == 'L':
        # print(f"lower half - {i} {range_start} {mid}")
        return search(i+1,range_start,mid, boarding_pass)
    if boarding_pass[i] == 'B' or boarding_pass[i] == 'R':
        # print(f"upper half - {i} {mid+1} {range_end}")
        return search(i+1,mid+1,range_end,boarding_pass)

inputfile = open("input.txt").readlines()
list_ids = []
for boarding_pass in inputfile:
    row = search(0, 0, 127, boarding_pass[0:7])
    column = search(0,0,7,boarding_pass[7:10])
    seat_id = row*8+column
    bisect.insort(list_ids,seat_id)
    # print(f"row:{row}, column{column}, ID:{seat_id}")
print(max(list_ids))

# Part 2
print(set(range(list_ids[0], list_ids[-1])) - set(list_ids))