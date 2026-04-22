
# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

# 5번 반복하는 반복문
# for i in range(6,1,-1):
#     print(f"숫자 : {i}")
# print("========================")

# for ch in "hello":
#     print(ch)

# for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"]:
#     if name.startswith("이"):
#         print(name)

# #문제 1 . 1부터 10 까지의 총합을 구하세요. 반복문을 사용해서
# num=0
# for i in range(1,11):
#     num += i
# print(f"총합 : {num}")

#문제 2 . ["15,000","13,000","8,700", "9,000", "25,000"]
#배열에 출금 금액들이 저장되어있다.
#만원 이상 금액들에 대해 출력하세요

# for price in ["15,000","13,000","8,700", "9,000", "25,000"]:
#     if int(price.replace(",","")) >= 10000:

#         print(f"출금 : {price}원")
#     else:
#         print(f"입금 : {price}원")

# money = ["15,000","13,000","8,700", "9,000", "25,000"]

# for i, v in enumerate(money):
#     print(i, v)     

#문제3. [89, 56, 78, 92, 61, 96, 83, 74]
#203호 학생들의 성적이다. 성적의 총 합과 평균을 출력하세요
# score = [89, 56, 78, 92, 61, 96, 83, 74]
# total = 0
# for i in score:
#     total += i
# print("총합 : ",total)
# print("평균 : ",total/int(8))
# print("평균 : ",total/len(score))

# for i,v in enumerate(score):
#     total=total+v
#     if v>=80:
#         print("80점 이상 학생 위치 : ",i )
# print("총점 : ",total)
# print("평균 : ", total/len(score))


#반복문 while
# while 조건:
#     실행코드
# while 문은 조건식이 참인 경우에 동작 하기 때문에
# 쉽게 무한루프에 들어갈수있다.
# 하여 while문 사용시 중단시킬수 있는 break를 같이 사용하는게 좋다.
# num = 5
# while num > 2:
#     print(f"2보다 크다")
#     break

# while True:
#     num += 1 #num = num + 1
#     if num ==7: continue #건너뛰기
#     print(num)
#     if num >= 10:
#         break

# while True:
#     cmd = input("명령어 : ").strip().lower()
#     if cmd == "history":
#         print("모든기록 출력")
#     elif cmd == "mkdir":
#         print("새로운 폴더 만들기")
#     elif cmd == "remove":
#         print("파일 제거")
#     elif cmd == "exit":
#         print("프로그램 종료")
#         break
#     else:
#         print("존재하지 않는 명령어 입니다.")

#파이썬 랜덤 사용
# import random
# com = random.randint(1,2)
# print(com)
# 동전 앞면 뒷면 맞추기 게임 만들기

# while True:
import random  
#     com = random.randint(1,2)
    
#     user = int(input("동전맞추기 : "))
#     if com == user:
#         print("맞춤")
#         print(com)
#     else:
#         print("틀림")
#         print(com)

# 가위바위보 게임 5판 진행
# 5번 게임 끝나면 몇판 몇승 몇패 몇무 인지 출력
win = 0
lose = 0
draw = 0
def compare(a,b):
    if a>b: return 1
    elif a<b: return -1
    else: return 0

game=["가위","바위","보"]

for i in range(5):    
    com = random.choice(game)
    user = input("가위바위보 : ").strip().lower()
#     if com == user:
#         print(com)
#         print("비김")
#         draw += 1
#     elif com == "가위" and user == "보":
#         print(com)
#         print("이김")
#         win += 1
#     elif com == "바위" and user == "가위":
#         print(com)
#         print("이김")
#         win += 1
#     elif com == "보" and user == "바위":
#         print(com)
#         print("이김")
#         win += 1
#     else:
#         print(com)
#         print("졌다...")
#         lose += 1
#    print(f"5판 중 {win}판 승리 {draw}판 비김 {lose}판 짐")

    print("컴퓨터 : ",com,"나 : ",user)
    #승패 무 판단
    #game.index("가위")
    #사전적 순서 비교 방법은 비교 연산자
    cidx = game.index(com)
    uidx = game.index(user)

    comp= cidx - uidx #유저와 컴의 가위바위보 값 비교
    #가위-0,바위-1,보-2 -> 유저가 0컴퓨터가 1이라면 컴으이 승
    # 즉 comp에 1이 있다면 컴의 승

    if com==user:
        print("비김")
        draw+=1
    elif comp== -1 or comp==2:
        print("나의승")
        win+=1
    else:
        print("나의 패")
        lose+=1
print("승 : ",win," 패 : ",lose, " 무 : ",draw)
