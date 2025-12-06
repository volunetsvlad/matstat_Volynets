A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
print("Масив A:", A)
print("Масив B:", B)

if len(A) != len(B):
    print("Масиви повинні мати однакову довжину")
else:
    add = [A[i] + B[i] for i in range(len(A))]
    sub = [A[i] - B[i] for i in range(len(A))]
    mul = [A[i] * B[i] for i in range(len(A))]
    div = [A[i] / B[i] for i in range(len(A))]

    print("\nАрифметичні операції")
    print("A + B =", add)
    print("A - B =", sub)
    print("A * B =", mul)
    print("A / B =", div)

C = A + B
print("\nМасив після конкатенації")
print("C =", C)

maximum = max(C)
minimum = min(C)
totalsum = sum(C)

product = 1
for x in C:
    product *= x

print("\nМаксимальний елемент C:", maximum)
print("Мінімальний елемент C:", minimum)
print("Сума елементів C:", totalsum)
print("Добуток елементів C:", product)
