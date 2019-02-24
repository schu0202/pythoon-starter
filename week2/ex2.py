# [문제2] 평균값 계산
A = [30, 40, 50, 60, 20, 10, 50]

def average(num):
    sum = 0
    for i in num:
        sum += i
    print(sum / len(num))

average(A)
