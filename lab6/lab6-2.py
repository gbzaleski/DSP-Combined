file = open("input.txt", "r")
data = file.read()
print(f"{round(data.count('G') * 100 / len(data), 2)}% G occurences")
print(f"{round(data.count('C') * 100 / len(data), 2)}% C occurences")