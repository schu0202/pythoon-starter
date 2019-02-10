#[문제1] 학급의 평균 점수

A = [70, 60, 55, 75, 95,90, 80, 80, 85, 100]
sum = 0
for i in A:
    sum+=i
print(sum/len(A))