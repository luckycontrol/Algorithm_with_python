# 시험 점수 구하기

# 시험 점수를 입력받아 점수에 해당하는 학점을 반환합니다.
# 90 ~ 100 -> A
# 80 ~ 89 -> B
# 70 ~ 79 -> C
# 60 ~ 69 -> D
# 나머지 -> F

def checkScore(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False

def getGrade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'

    return 'F'

while True:

    score = input()
    if(checkScore(int(score))):
        break

print(getGrade(int(score)))
