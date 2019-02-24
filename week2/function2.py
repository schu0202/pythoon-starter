# 혈액형의 갯수를 리턴받는 함수
def getCountBlood(blood):
    bloodList = ['A', 'B', 'AB', 'O', 'O', 'AB']
    count = 0

    for name in bloodList:
        if name == blood:
            count +=1
    return count

blood_ipout = input()
result = getCountBlood(blood_ipout)
print(result)