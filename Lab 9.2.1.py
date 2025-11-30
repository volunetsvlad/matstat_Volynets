n = int(input("Введіть п'ятизначне число: "))

a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10

first = a + c + e
second = b + d

print(int(f"{first}{second}"))