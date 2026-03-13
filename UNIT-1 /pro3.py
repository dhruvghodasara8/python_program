#write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

sub1 = float(input("Enter marks of maths: "))
sub2 = float(input("Enter marks of science: "))
sub3 = float(input("Enter marks of english: "))
sub4 = float(input("Enter marks of hindi: "))

total = sub1 + sub2 + sub3 + sub4 
percentage = total / 4

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n----- Result -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
