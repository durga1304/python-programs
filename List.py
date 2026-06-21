def get_grade(score):
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'

students = ["Shrushti", "Durga", "Akshara", "Sanu"]
marks =[85,78,90,92]

for i in range(len(students)):
    grade = get_grade(marks[i])
    print(f"{students[i]} score {marks[i]} and received grade {grade}")


    
