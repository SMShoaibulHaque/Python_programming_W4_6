print("Program starting.")
i = int(input("Insert a positive integer: "))
steps = 0
while i != 1:
    print(i, end=" -> ")
    if i % 2 == 0:
        i = i // 2
    else:
        i = i * 3 + 1
    steps = steps + 1
print(i)
print(f"Sequence had {steps} total steps.")
print()
print("Program ending.")
