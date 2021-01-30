# File for quick testing while coming up with ideas

#==============================================
# Testing grid creation and printing
rows = 6
columns = 9
grid = []

for number in range(rows):
    grid.append(["[ ]"] * columns)

print("Testing Grid creation")
for row in grid:
    print(" ".join(row))
#==============================================

userInputtedVal = 0
while userInputtedVal != 1:
    userInput = input("Enter Column: ")
    userInputtedVal += 1