# 파일을 읽어들일때 함수가 3가지가 있다.
# readline() -> 한줄씩 읽어들인다.
# readlines() -> 리스트 형태로 바꿔준다
# read()  -> 스트링 형태로 다 읽어들인다.

f = open("새파일.txt", 'r')
data =f.read()
print(data)
f.close()






