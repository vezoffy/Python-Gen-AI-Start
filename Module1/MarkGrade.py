mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))
mark4 = int(input("Enter marks for subject 4: "))
mark5 = int(input("Enter marks for subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print(f"Total marks: {total}")
print(f"Average marks: {average}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")