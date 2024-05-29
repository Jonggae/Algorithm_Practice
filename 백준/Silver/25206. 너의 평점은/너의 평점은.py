n = 20
sumOfMultiple = []
sumOfScore = []

# 전공평점 :  전공 과목별 (학점 x 과목평점)의 합을 학점의 총합 으로 나눈 값
for _ in range(n):
    subject, score, grade = input().split()
    score = float(score)

    if grade == "A+":
        grade = 4.5
    elif grade == "A0":
        grade = 4.0
    elif grade == "B+":
        grade = 3.5
    elif grade == "B0":
        grade = 3.0
    elif grade == "C+":
        grade = 2.5
    elif grade == "C0":
        grade = 2.0
    elif grade == "D+":
        grade = 1.5
    elif grade == "D0":
        grade = 1.0
    elif grade == "F":
        grade = 0
    if not grade == "P":
        sumOfMultiple.append(score * grade)
        sumOfScore.append(score)

A = sum(sumOfScore)
B = sum(sumOfMultiple)
print(B/A)