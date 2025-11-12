line1 = "59912|Withdraw|1000\n"
line2 = "59913|Deposit|2000\n"
line3 = "59914|Deposit|3000\n"

f = open("transactions.txt", "w+")
f.writelines([line1, line2, line3])
f.close()

f = open("transactions.txt", "r")
print(f.read())
f.close()