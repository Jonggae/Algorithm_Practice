import sys
n = int(sys.stdin.readline())

score = list(map(int, input().split()))
maxScore = max(score)
fixedScore = []

i=0
while i<len(score):
    fixedScore.append(score[i]/maxScore*100)
    i+=1

avg = sum(fixedScore)/len(fixedScore)
print(avg)
