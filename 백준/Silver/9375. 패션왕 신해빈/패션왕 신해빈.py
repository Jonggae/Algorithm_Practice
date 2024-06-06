
n = int(input())


# 각 테스트별로 {신체 : 의상} 으로 저장
def do_test():
    clothes_dict = {}
    num = int(input())
    for i in range(num):
        acc, body = input().split()
        if body not in clothes_dict:
            clothes_dict[body] = []
        clothes_dict[body].append(acc)
    return clothes_dict


# 결국 경우의 수 구하는게 어려웠음..
def find_combination(c):
    com = 1
    for body in c:
        com *= (len(c[body]) + 1)
    return com - 1


for _ in range(n):
    clothes = do_test()
    print(find_combination(clothes))