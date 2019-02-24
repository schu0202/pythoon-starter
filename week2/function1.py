# 함수를 만들때는 def 라고 함수를 정의 한다.
# 함수의 기본목적은 공통으로 사용한다.

# 더하기를 해주는 함수를 만들고 싶다.

# def 함수명(매개변수)
# def sum(i, j):
#      print(i+j)
#
# sum(3, 5)

# 지역변수 -> 함수안에서 특정부분 내에서만 사용 할 수 있는 변수
# 전역변수 -> 지역변수가 아닌 모든 곳에서 사용하는 변수
# 밖에 있는 변수명 안에 있는 변수명이 겹칠때 빡에 있는 변수명이 아니다라는건 알고 가자
# global a # 전역변수
# def sum(a,b):
#      print(a+b)
# a = 3 #지역변수
# b = 5 #지역변수
# sum(a,b)

# 매개변수값에 값이 안 넘어오는 경우에 디폴트값을 지정해 줄 수 있다.
# def sum(i, j = 0):
#     print(i+j)
# sum(3)

# return은 호출한에게 값을 돌려줄때 사용한다.
# 함수인에 retutn 이 있을수도 없을수도 있다. 개발자마음에 따라
# def sum(a,b):
#     return a+b
#
# result = sum(3,4)
# print(result)
#