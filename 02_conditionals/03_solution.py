
score = int(input("Tell your score: "))

if score >= 101:
    print("Verify your score")
    exit()

elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"    

print("Grade: ",grade )
    