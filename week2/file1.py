# 파일을 생성하거나 열때는 open 이라는 함수를 이용한다.
# open 함수의 첫번째 매개변수값은 파일의 이름 두번째 매개변수 값은 모드
# 모드 w = 쓰기 모드, a = 추가모드, r = 읽기모드
# 파일이 존재하지 않으면 파일을 새로 생성하고
# 파일이 존재하면 파일을 덮어씌운다(w모드) 파일에 내용을 추가한다(a모드)
# 변수명.writre 파일에 내용쓰기
f = open('새파일.txt', 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

