#==============================================
# Testing grid creation
rows = 6
columns = 9
grid = []

for number in range(rows):
    grid.append(["[ ]"] * columns)

print("Testing Grid creation")
for row in grid:
    print(" ".join(row))
#==============================================