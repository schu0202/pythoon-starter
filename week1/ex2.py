# 리스트에 혈액형이 있는데
# 각 혈앵형별 개수가 궁금해요

bloodList = ['A','B','AB','O','O','AB']
acount=0;
bcount=0;
ccount=0;
dcount=0;
#hint
#변수가 최소 4개 나와야한다.

for name in bloodList:
    if(name=='A'):
        acount+=1
    elif(name=='B'):
        bcount += 1
    elif (name == 'O'):
        ccount += 1
    elif (name == 'AB'):
        dcount+=1
print("A형: {}, B형: {}, AB형: {}, O형: {}".format(acount,bcount,ccount,dcount))
