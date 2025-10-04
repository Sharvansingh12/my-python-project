correct=int(input("Enter the Number of correct answers: "))
wrong=int(input("Enter the Number of wrong answers: "))
unattempted=int(input("Enter the Number of unattempted questions: "))

score=(4*correct)-wrong

if score>=180:
    per="Excellent"
    
elif 120<=score<=179:
    per="Good"
    
elif 60<=score<=119:
    per="Average"
    
else:
    per="Fail"

print(f"Performance Level: {per}")

if correct<wrong:
    print("Note: Improve Accuracy!!!")