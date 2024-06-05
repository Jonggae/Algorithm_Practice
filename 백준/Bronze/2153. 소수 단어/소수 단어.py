# 알파벳을 숫자로 표현하여 소수단어를 확인
import math

word = list(input())


# 대 소문자를 문제에서 원하는 숫자로 표현함
def lower_to_number(a):
    return ord(str(a)) - 96


def upper_to_number(a):
    return ord(str(a)) - 38


def char_to_num(a):
    ascii = ord(str(a))
    if 90 >= ascii >= 65:
        return upper_to_number(a)
    else:
        return lower_to_number(a)


def check_prime(n):
    if n < 1:
        return False
    if n == 1:
        return True  # 이 문제에서만 1을 소수로 인정
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # n의 제곱근 까지의 숫자로 나누어 떨어지는가?
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


sum = 0
for i in range(len(word)):
    sum += (char_to_num(word[i]))

if check_prime(sum):
    print("It is a prime word.")
else:
    print("It is not a prime word.")