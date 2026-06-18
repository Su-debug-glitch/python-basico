import os
os.system("cls")

print("---RANGE()---")

for num in range(10):
    print(num)

# range(inicio, fin)
print("---RANGE(inicio, fin)---")
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
print("---RANGE(inicio, fin, paso)---")
for num in range(0, 10, 2):
    print(num)

# range() con negativos
print("---RANGE() con negativos---")
for num in range(-10, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

# De range a list
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# repetir algo con range (en lugar de hacer un bucle while, por ejemplo)
for _ in range(5):
    print("hacer algo 5 veces")