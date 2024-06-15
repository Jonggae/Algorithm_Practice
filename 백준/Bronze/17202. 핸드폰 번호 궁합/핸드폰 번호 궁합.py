n = 8
num1 = list(map(int, input()))
num2 = list(map(int, input()))


def merge_list(list1, list2):
    long_num = []
    for i in range(n):
        long_num.append(list1[i])
        long_num.append(list2[i])
    return long_num


long_num = merge_list(num1, num2)


def sum_number(list):
    if len(list) == 2:
        return list

    sum_nums = []
    for i in range(1, len(list)):
        sum_nums.append((list[i] + list[i - 1]) % 10)

    return sum_number(sum_nums)

answer = sum_number(long_num)
print(str(answer[0])+str(answer[1]))
