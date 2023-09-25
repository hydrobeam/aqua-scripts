### builds a cartesian product table of two things, change rows/cols as desired
### also will produce the generating series that corresponds to th

from collections import Counter

tot_table = []
rows = 6
cols = 6
func = lambda x, y : x * y

# slightly faster than extend & cell approach
def flatten(table: list[list[int]]) -> list[list[int]]:
    new_table = []
    for row in table:
        new_table += row
    return new_table

# can produce a flattened table here,
# but keep a prettified version and flatten later
for i in range(1, rows + 1):
    tot_table.append([])
    for j in range(1, cols + 1):
        tot_table[i - 1].append(func(i, j))

out_str = ""

for val, occurences in Counter(flatten(tot_table)).items():
     out_str += (f"{occurences}x^{{{val}}} + ")

