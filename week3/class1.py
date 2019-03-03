# class 정의시 class 클래스명
# __init__은 클래스, 최초생성시 제일 먼저 실행된다.
# init에서는 속성값에 대한 초기화, 특정메서드 실행등의 행위가 들어간다.
# self는 클래스 호출한 그 자체
# 함수는 공통적으로 사용하기 위한 것이고 클래스 함수 기능뿐만 아니라 속성값도 받아올 수 있다.
# 클래스 생성시 값을 넘겨줄수 있다.
# __intit__에서 매개변수로 받는데 첫번째 self가 아닌 두번째부터 매칭된다.

class magician:
    def __init__(self, item):   #self는 클래스 호출한 그자체이며 고정이다, 매개변수를 추가로 입력 가능
        # 속성값 정의
        self.max_hp = 150
        self.hp = 100
        self.mp = 200
        self.str = 5

    def attack(self):
        if(self.str > 5):
            print("공격!공격!")
        else:
            print("공격!")

    def drink_potion(self):
        if(self.hp + 30 > self.max_hp):
            self.hp = 150
        else:
            self.hp += 30


char1 = magician('item') # 클래스 생성
char1.attack() # 클래스 메소드(함수)를 사용
char1.drink_potion()
char1.drink_potion()

print(char1.hp)

