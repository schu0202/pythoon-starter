#[문제1] 홀수 짝수 판별
def is_odd(num):
    if(num % 2 == 1): # 홀수일경우
        print('홀수입니다')
    else: #홀수를 제외한 나머지는 짝수이다
        print('짝수입니다')

number = int(input())
odd = is_odd(number)
print(odd)

