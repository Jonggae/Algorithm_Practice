n = int(input())
peaks = list(map(int, input().split()))


def shoot_bow(peaks):
    score = 0
    kill = 0
    current_peak = peaks[0]
    for i in range(1,len(peaks)):
        if current_peak > peaks[i]:
            kill+=1
        else: # 현재봉우리보다 높은것을 만나면
            current_peak = peaks[i]
            kill = 0
        score = max(kill,score)
    return score

print(shoot_bow(peaks))
