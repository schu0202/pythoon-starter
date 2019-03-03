# 게임 캐릭터가
# 속성값
# level, hp, mp
# exp //경험치
# hp_potion //hp포션 갯수
# mp_potion /mp포션 갯수

# 메소드값
# attack()
# - "공격하였습니다" 메시지 출력
# - exp 50씩 증가하면서 100이 되면 레벨업 메소드를 실행 해준다.
# Level_up()
# -  레벨을 1 씩 증가시켜준다.

class character:
    def __init__(self):
        self.level = 5
        self.exp = 0
        self.hp = 50
        self.mp = 30
        self.hp_potion = 5
        self.mp_potion = 3

        self.init()

    def init(self):
        print("재정의")

    def attack(self):
        print("공격하였습니다")
        self.level_up(50)

    def level_up(self, exp):
        self.exp += 50

        if self.exp >=100:
            self.level +=1
            self.exp = 0

    def drink_protion(self, mode):
        if( mode == 'hp'):
            self.hp_potion -= 1
            self.hp +=30
        elif mode == 'mp':
            self.mp_potion -= 1
            self.mp += 30

# 공통적인 클래스를 상속받아 직업을 만들어 봅시다
# magician 클래스를 하나 생성하고 공통 내용을 상속받는다.
# magician 값은 500으로 초기화
# skill_level 값은 1
 # 메소드
 # do_skill() 사용시
 # skill_level이 1씩 증가하고
 # skill_level의 데미지는 스킬레벨*10;
 # drink_potion 오버라이딩 hp 와 mp가 50씩 찬다.

class magician(character):
    def init(self):
        self.skill_level = 1

    def do_skill(self):
        damage = self.skill_level * 10
        self.mp -= 30
        self.skill_level +=1
        print("스킬")
        return damage

    def drink_protion(self, mode='hp'):
        if( mode == 'hp'):
            self.hp_potion -= 1
            self.hp +=50
        elif mode == 'mp':
            self.mp_potion -= 1
            self.mp += 50

char1 = character()
char1.attack()
print(char1.level)

char2 = magician()
char2.do_skill()
char2.drink_protion()

print(char2.level)
print(char2.skill_level)
