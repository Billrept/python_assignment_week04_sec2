grades = [55, 70, 65, 40, 90, 85, 50, 77]

passed_with_bonus = [grade + (grade*5/100) if grade >= 60 else grade for grade in grades if grade >= 60]
print(passed_with_bonus)