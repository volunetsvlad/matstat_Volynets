count = 0

previous = int(input())
current = int(input())

while current != 0:
    if previous > current:
        count += 1
    previous = current
    current = int(input())

print(count)