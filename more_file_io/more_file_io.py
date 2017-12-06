import os
import random

path = 'data'

file_names = os.listdir(path)

for i, f in enumerate(file_names):
    print(str(i) + ") '" + f)

print()

choice = input("pick a category ")
choice = int(choice)

print()

file = path + "/" + file_names[choice]
print(file)

with open(file, 'r') as f:
    lines = f.read().splitlines()

print(lines)
print()

category_name = lines[0]
puzzle = random.choice(lines[1:])

print(category_name)
print(puzzle)
