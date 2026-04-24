# 리스트, 튜플
# 리스트 - 여러 데이터를 저장 관리 하기 위한 파이선 자료 구조 이다.
# 튜플도 리스트와 같은데 차이점은 리스트는 수정이 가능하지만 튜플은 수정이 불가능하다.

# #리스트
# number = [10,20,30,40,50]
# empty = []
# name =list()

# print( number[0])
# print( number[-2])

# # 리스트 자르기
# num = number[2:4]
# print(num)
# num2 = number[3:]
# print(num2)
# num3 = number[:3]
# print(num3)

# # 리스트 수정
# number[2] = 60
# print(number)

# # 리스트 추가
# number.append(70) #리스트 마지막에 추가
# print(number)

# number.insert(2,500) #리스트에 원하는 위치에 추가(인덱스, 값)
# print(number)



# # 리스트 값 삭제
# number.remove(500) #리스트에서 삭제 할 데이터 입력
# print(number)

# number.pop(1) #리스트에서 삭제할 데이터의 인덱스 입력
# print(number)

# del number[1] #인덱스로 삭제
# print(number)

# #리스트 크기 (길이)
# print(len(number))

# for num in number:
#     print(num)

# for i, num in enumerate(number):
#     print(i, num)

# # 리스트 검색
# print( 40 in number) #값의 존재여부 true, false
# print( 30 not in number)
# print( number.index(50)) # 인덱스 찾기 - 없으면 오류
# #인덱스를 통해 인덱스를 찾기 전에 in으로 존재여부 확인 먼저 하기

# #리스트 정렬
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number)

#리스트는 일반적으로 많이 사용되는 자료 구조이다.'
# 자바에서 list (ArrayList)를 많이 사용된다면 파이썬은 리스트이다.,
# 여러 데이터를 저장할수 있고 , 수정 , 추가 가능하고 반복문 사용 쉽고
# 정렬, 검색도 되고 그래서 사용하기 좋은 녀석이다.!

#리스트 문제 풀기!!
# 문제 1. 5명의 이름이 저장되어있는 리스트 만들기
# 5명의 이름 출력하는 반복문 만들기

# list = ["짱구", "맹구", "철수", "훈이", "유리"]
# print(type(list))
# for name in list:
#     print(name)

# #\문제 2. 짱아 이름을 추가하고 출력하세요
# list.append("짱아") #원하는 위치 추가는 insert

# print(list)

# # 문제 3. 리스트에 철수 있는지 확인하는 코드 작성하기

# # print("철수" in list)

# if "철수" in list:
#     print("등록된 이름이다")
# else:
#     print("등록된 이름이 아니다.")

# # 문제 4. 이름 리스트에 내림차순으로 정렬 하여 출력하세요

# list.sort(reverse=True)
# print(list)

# 문제 5. 과일 이름이 두글자인 과일만 출력하세요 
# fruits = ["사과","바나나","파인애플","딸기","오렌지","포도","배"]

# for fruit in fruits:
#     if len(fruit) == 2:
#         print(fruit)

# fruits.sort(key=len, reverse=True)
# print(fruits)

# #문제 6 . 과일 검색 프로그램 만들기
# # 과일을 키보드를 통해 입력받는다.

# while True:
#     user = input("과일 이름 : ").strip()
#     if user == "종료":
#         break
#     elif user in fruits:
#         print((user),"판매중")
#     else:
#         print((user),"품절")

# fruits.sort() # 딸기 바나나 배 사과 오렌지 파인애플 포도
# price = [5000, 8000, 12000, 9500, 15500, 20400, 9000]

# #문제 7. 구매할 과일을 입력하면 총 지불 금액 얼마인지 출력
# # 단, 과일은 1개를 구매할수도 있고 여러개 구매할수도 있어야한다.
# total = 0
# while True:
#     user = input("과일이름 : ").strip()
    
#     if user == "종료":
#         print(f"총금액 : {total}원")
#         break
   
#     elif user in fruits:
#         p = (fruits.index(user))
#         print(f"{price[p]}원")
#         total += price[p]
#     else:
#         print((user),"매진")

#튜플 - 리스트처럼 여러 데이터를 저장 할수 있는 자료형 이다.
# 저장한 데이터를 수정할수 없다.
# 데이터를 보호 하기 위한 목적
# 속도와 메모리 효율성
# 딕셔너리의 키로 사용
#여러개의 값을 반환(return) 시킬때

# 튜플 만들기
# number= (10,20,30,40) #작은괄호 - 튜플 , 대확호 - 리스트
# print(number)
# print(type((1,2,3,4)))
# print(type((10,)))

# # 튜플 슬라이싱 (자르기)
# num = number[2:4]
# print(num)

# # 튜플 검색
# print(40 in number)
# print(number.index(40))

# # 리스트와 다른점
# # 수정불가 , 추가 불가
# # number.append(50) 오류
# # number.remove(50) 오류
# # number.pop(50) 오류
# # del number[2] 오류

# print( number.count(20  )) #특정값 갯수 구하기

# data = 10,20,30,40 # 패킹 - 여러값을 하나로 묶기
# print(type(data))

# a,b,c,d = data # 언패킹 - 묶여있는 값을 여러개로 나누기
# print(a,b,c,d)

# red =20
# blue = 10

# red, blue = blue,red
# print(red,blue)

# #함수 반환 여러개
# def get():
#     return 10,20,30

# 리스트 <-> 튜플
info = ("다음주", "금요일","빨간날","그래서","우리는","5월6일에","봐요")

# info[0] ="이번주"

info_list = list(info) #튜플 -> 리스트로 변환
info_list[0] = "이번주"

info = tuple(info_list) #리스트 -> 튜플로 변환
print(info)