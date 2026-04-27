# 딕셔너리
# 딕셔너리는 데이터를 키와 value로 저장하는 자료형 이다.

# info = {"name" : "이순신"}
# print(info["name"])

# m = ["이순신", 34, "군인"]

# print(m[0])
# print(m[1])
# # m[0]-> 이름인지 , 나이인지 , 직업인지 알수가 없다.

# info = {"name" : "이순신", "age" : 34, "job" : "군인"}
# print(info["name"])
# print(info["age"])
# print(info["job"])

# #딕셔너리는 언제 사용하냐?? 
# # 로그인 회원이나, 상품정보, 단일 게시글 정보 , 설정값
# # JSON데이터, API응답 데이터용

# name = dict()

# print( info.get("city")) #get 사용시 오류 x none

# info["city"] = "대전" #딕셔너리에 키와 값 추가

# print(info)

# city = info.pop("city") #딕셔너리에서 키와 값 삭제
# print(city)
# print(info)
# del info["age"]
# print(info)

# if "name" in info: # 딕셔너리에서 키 존재 여부 확인

#     print("이름이 있따")

# if "김유신" in info.values():

#     print("김유신이 있따")

# k , v = info.items() #딕셔너리에서 키와 valye 가져오기
# info.keys() #딕셔너리에서 키만 가져오기

# print( type(k),type(v) )
# print(k,v)

# #딕셔너리에 key로 사용가능한것
# # 문자열, 정수, 실수, 튜플

# info= {
#     "id" : 1004,
#     "email" : "hahaha@naver.com",
#     "name" : "이순신",
#     "birth" : "200010424",
#     "addreess" : "대전광역시 중구 선화동 방산빌딩 2층 203호"

# }
# # 이름이 이순신이냐?
# if "name" in info:
#     if info["name"] =="이순신":
#         print("이순신이다")
#     else:
#         print("이순신이 아니다")
# else:
#     print("이름 정보가 없다")

# # 이메일의 도메인은 무엇인가?

# if "email" in info:
#     email = info["email"]
#     domain = email[email.index("@")+1:]
#     print(domain)

#     # domain = email.split("@")[1]
#     # print(domain)

# # 주소가 잘못 저장 되었다. 선화동이 아니라 대흥동 이다 수정하시오

# if "addreess" in info:
#     addr = info["addreess"]
#     addr = addr.replace("선화동","대흥동")
#     print(addr)
#     info["addreess"] = addr
# print(info)

# nums = []
# for i in range(1,5):
#     nums.append(i * 2)

# print(nums)

# # 컴프리핸션  range(1,5) -> [1,2,3,4] //i*2 라서 [2 4 6 8]
# # [표현식 for 변수 in 반복대상]

# nums2 = [i*2 for i in range(1,5)]
# print(nums2)

# # 1~15 까지 숫사중에서 3의 배수만 리스트에 저장하겠다

# nums3 = [i for i in range(1,16) if i % 3 == 0]
# print (nums3)

# cost = [4500, 6700, 3100, 5800, 2700, 4900]
# # cost 리스트에는 상품의 가격이 저장 되어있다.
# # 5000원 이하는 저가형 , 5천원 초과는 고가형상품 이라고 저장하시오
# #if~else 를 표현식에 쓰는경우
# #[저장값 if 조건식 else 저장값 for 변수 in 반복대상]
# result = [ "저가형" if p <= 5000 else "고가형" for p in cost ]

# print(result)

# 학생 성적 관리 프로그램 만들기.  과목 국어 , 수학, 영어
# std1 = [89, 56, 73]
# std2 = [45, 87, 35]
# std3 = [67, 78, 90]
# std4 = [89, 56, 73]
# std5 = [45, 87, 35]
# stdName = ["이순신","임꺽정","한석봉","정약용","김춘추"]

# std = std1,std2,std3,std4,std5

# print(std) 

# score = dict()
# # 과목명 튜플
# subject = ("국어","수학","영어")

# for i,name in enumerate(stdName):
#     temp = dict()
#     for k,s in enumerate(std[i]):
#         temp[subject[k]] = s
#     score[name] = temp
# #한석봉 학생의 성적을 출력하시오
# print (score["한석봉"])
# for k,v in score["한석봉"].items():
#     print(k,v)

# print(score)


# {"이순신":{"국어":89,"수학":56,"영어":73},
# "임꺽정":{"국어":45,"수학":87,"영어":35},
# "한석봉":{"국어":67,"수학":78,"영어":90},
# "정약용":{"국어":89,"수학":56,"영어":73},
# "김춘추":{"국어":45,"수학":87,"영어":35}
# }

# 문제 1. 딕셔너리를 만드세요

# snackName = ["새우깡","칙촉","마가렛","짱구","포카칩","초코하임"]
# price = [2000, 3200, 4500, 3000, 2800, 4200]

# snack = dict()

# for i,v in enumerate(snackName):
#     snack[v] = price[i]
# print(snack)

# snack2 ={v:price[i] for i,v in enumerate(snackName)}
# print(snack2)


#문제 2. 딕셔너리를 만들고 다음 조건으로 조회 하세요
item=["선풍기","냉장고","에어컨","Tv","컴퓨터","노트북","청소기"]
brand = ["LG","삼성","LG","삼성","HP","DELL","다이슨"]
price = [80000, 1250000, 850000, 1540900, 2300000,1570000, 534000]

# item, brand, price 의 각 인덱스 매칭이다.
# 선풍기는 lg이고 금액은 80000원이다.
# 딕셔너리의 키는 제품명 value는 브랜드와 금액
# 삼성 브랜드의 제품명과 금액을 출력하세요

# p = dict()
# for i in range(len(item)):
#     p[item[i]] = {"브랜드":brand[i],"가격":price[i]}
# from pprint import pprint
# pprint(p)
# for name, info in p.items():
#     if info["브랜드"] == "삼성":
#         print(name,info["가격"])
    
# set - 중복 허용하지않고, 순서가 없는 자료형
# 데이터 정리, 검색

# data ={1,2,3,4,5, 3,4,5,3,4,5 }
# print(data)
# set1= set() #비어있는 set 만들기    

# list = ["이순신","임꺽정","한석봉","정약용","김춘추"]

# set2 = set(list)
# print(set2)
# #print (set2[1])#인덱스 접근 불가

# set2.add("장영실") #set에 값 추가
# print(set2)

# set2.update(["이성계","문익점","세종"]) #여러개 추가
# print(set2)

# set2.remove("장영실") #삭제 - 존재 하지 않을 시 오류
# print(set2)

# set2.discard("장실") #삭제 - 존재 하지 않을 시 오류 x
# print(set2)

# set 안에 값이 존재하냐 -> in

# 교집합, 합집합, 차집합

# a = {"복숭아","배","메론","체리","포도"} #도헌이가 좋아하는 과일
# b = {"사과","배","딸기","바나나"} #찬용이가 좋아하는 과일
# c = {"바나나","참외","사과","귤","포도","딸기","토마토"}#현규가 좋아하는 과일

# print(a|c) #합집합
# print(a&b) #교집합
# print(b-c) #차집합
# print(a^c) 

# for fruit in c:
#     print(fruit)

'''
 list - 다수의 데이터 저장용으로 많이 사용, 중복 허용 , 추가 수정 삭제 가능
 tuple - 다수의 데이터 저장 가능 , 중복허용, 추가 수정 삭제 불가능 
 dict - key:value 구조 , key는 중복 안됨
 set - 중복허용하지 않음, 순서 없음 , 검색, 그룹(집합)에 사용

'''
#과일가게 재고 관리 프로그램

# 과일 데이터 
import random

fruits =[
    {"name":"사과", "price":3000, "stock":20},
    {"name":"바나나","price":1500, "stock":30},
    {"name":"포도","price":5000, "stock":11},
    {"name":"복숭아","price":4000, "stock":8},
    {"name":"수박","price":9900, "stock":34}
]

sales = list() #판매기록 용
admin = {"id":"admin", "pw":"1234"} #관리자 계정

print("\n================과일 재고 관리 프로그램====================\n")

userId = input("아이디 : ").strip().lower()
userPw = input("비밀번호 : ").strip()

if userId == admin["id"] and userPw == admin["pw"]:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호가 잘못되었습니다.")
    exit()
#로그인후 메뉴 실행

while True:
    print("\n====메뉴====")
    print("1. 과일 목록 보기")
    print("2. 과일 검색")
    print("3. 과일 판매")
    print("4. 재고 확인")
    print("5. 과일 추천")
    print("6. 판매 기록 보기")
    print("0. 프로그램 종료")

    menu = input("메뉴 선택 : ").strip()
    if menu == "1":
        print("\n====과일 목록====")
        for fruit in fruits:
            print(f"{fruit['name']}/ 가격 : {fruit['price']}원 / 재고 : {fruit['stock']}개")
            
       
    elif menu == "2":
        print("\n====과일 검색====")
        keyword = input("검색어 입력 : ").strip()

        result = [fruit for fruit in fruits if keyword in fruit["name"]]

        if result:
            for f in result:
                print(f["name"],f["price"],"원/ 재고",f["stock"],"개")
        else:
            print("검색 결과가 없습니다")
        
    elif menu == "3":
        name = input("판매한 과일 이름 : ").strip()
        count = int(input("판매 수량 : ").strip())

        found = False #판매한 과일이 과일 데이터에 있나 없나 확인
        for fruit in fruits:
            if fruit["name"] == name:
                found = True # 판매하고자 하는 과일이 있따.
                if fruit["stock"] >= count:
                    fruit["stock"] -= count # fruit["stock"] = fruit["stock"] - count
                #판매 내역을 튜플로 생성
                    sale = (name , count , fruit["price"]*count )
                    sales.append(sale) # 판매기록을 sales에 저장
                    print("판내 완료")
                    print(f"총 금액 : {fruit['price']*count}원")
                else:
                    print("재고가 부족합니다.")
        
        if not found: # 판매하고자 하는 과일이 없다.
            print("해당 과일이 없습니다.")

    elif menu == "4":
        # 과일들의 재고량을 확인하며 5개 이하인 과일들 찾아서 출력하기
        # 만약 5개 이하 인 과일이 없다면 재고 부족 과일이 없습니다. 라고 출력
        
        names = [fruit["name"] for fruit in fruits if fruit["stock"] <= 5]
        if names:
            print("===재고 부족한 과일들 (5개 이하)===")
            for name in names:
                print(f["name"], "/ 재고 : ", fruit["stock"], "개")
        else:
            print("재고 부족 과일이 없습니다.")


        # low = False
        # for fruit["stock"] in fruits:
        #     if fruit["stock"] < 5:
        #         low = True
        #         print( fruit["name"], "/ 재고 : ", fruit["stock"], "개")
                
        # if not low:
        #     print("재고 부족 과일이 없습니다.")
        
        
    elif menu == "5":
        # 오늘의 추천 과일 - 랜덤
        # import random - randint(1,10) : 1~10 사이 정수 , randrange(1,10) : 1~9사이 정수
        # random.choice(fruits) : 리스트 내분의 값을 하나 랜덤으로 추출
        # random.choices(fruits, k=3) : 리스트 내부의 값 3개 랜덤으로 추출(중복 허용)
        # random.sample(fruits, 4) : 리스트안에서 값중 4개를 랜덤 선택 ( 중복 없음 )
        # random.shuffle(fruits) : 리스트를 랜덤으로 순서 섞기
        # random.choices(fruits, weights = w, k=3) : 리스트 내부의 값 3개 확률( 가중치) 적용하여 랜덤으로 추출(중복 허용)
        # i=[1,2,3,4,5]
        # w = [0.2,0.3,0.4,0.5,0.6]

        # random.seed(10)
        # print(random.randint(1,100)) 

        recommend = random.sample(fruits,3)

        result = sorted(recommend, key = lambda x:x["name"])

        print("====오늘의 과일 추천====")
        for f in recommend:
            print(f"{fruit['name']}")
        
    elif menu == "6":
        #판매 기록 을 출력 - sales
        # 판매한 과일에 대해 출력, 총 판매 금액 출력
        print("====판매 기록====")
        total = 0 #총 판매 금액 저장용
        for sale in sales:
            name,count,price = sale
            print(f"{name} : {count}개, 총금액 : {price}원")
            total = total+price # total+=price

        print(f"총 판매 금액 : {total}원")

    elif menu == "0":
        print("\n====프로그램 종료====")        
        break
    else:
        print("잘못된 메뉴입니다.")

        
           
        