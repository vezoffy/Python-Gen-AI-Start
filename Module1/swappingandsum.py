l = []
n = (int(input("Enter the number of elements: ")))
for i in range(1, n + 1):
    l.append(int(input(f"Enter element {i}: ")))
print(f"Before swapping: {l}")
l[0], l[n - 1] = l[n - 1], l[0]
print(f"After swapping: {l}")
s = 0
for i in l:
    s += i
print(f"Sum: {s}")