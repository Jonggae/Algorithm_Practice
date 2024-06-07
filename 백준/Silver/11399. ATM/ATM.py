import itertools

n = int(input())  # 사람 수
time = list(map(int, (input().split())))  # 시간

# 누적된 시간의 총 합이 최소로 나오도록 times를 다시 정렬함

# 제시된 배열의 인덱스와 시간을 함께 저장
time_index = []
for i, index in enumerate(time):
    time_index.append([i, index])

# 예제 배열의 [인덱스, 시간]을 낮은 시간 순으로 정렬
sorted_time_index = sorted(time_index, key=lambda x: x[1])

# 인덱스만 뽑아옴
sorted_waiting_time_index = []
for i in sorted_time_index:
    sorted_waiting_time_index.append(i[0])


# 이 인덱스 값을 이용해서 그 인덱스에 해당하는 time의 값을 순서대로 누적하여 더함

def minimum_time(index, time):
    total_sum = 0

    temp_list = []
    for i in index:
        temp_list.append(time[i])
    cumulative_sums = list(itertools.accumulate(temp_list))
    total_sum = sum(cumulative_sums)
    return total_sum

print(minimum_time(sorted_waiting_time_index, time))