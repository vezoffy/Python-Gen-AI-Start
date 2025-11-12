f = open("customer.txt", "r")
num = 0
for i in f.readlines():
    num += 1
print(num)
f.close()