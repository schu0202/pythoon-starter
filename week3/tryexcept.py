# 예외처리
# 예외를 처리하기 위한것
# try except문
try:
    number = int(input())
except ValueError: #특정 에러를 잡기 위해 에러값을 넣어준다.
    print('숫자만 입력해라')

