# """if(i>5){ 자바, 자바스크립트 방법
    
# }else{

# }"""
# #if 조건식:
# #    실행할 코드

# num = 10
# if num > 5:
#     print("크다")
#     print("10이 크다")
# elif num < 5:
#     print("작다")
#     print("5보다 작다")

# # 변수 apple의 값이 10이상이라면 1봉지 8000원 라고 출력
# # apple의 값이 10미만이라면 개당 2000원

# apple = 10
# if apple >= 10:
#     print("1봉지")
#     print("8000원")
# else:
#     print("개당")
#     print("2000원")

# res=2
# match res:
#     case 1|4:
#         print("숫자1 또는 4이다")
#     case 2:
#         print("숫자2이다")
#     case int():
#         print("정수 이다")

# #like 좋아요 변수의 값이 100이상이면 spot 등록 출력
# #좋아요 변수의 값이 10 이하라면 관심 spot 출력

# like = 50
# if like >= 100:
#     print("spot 등록")
# elif like <= 10:
#     print("관심 spot")
# else:
#     print("spot 직전")

# #아이디 와 비밀번호 입력 받아 일치하면 로그인 성공, 불일치면
# #아이디 또는 비밀번호가 잘못 되었습니다. 출력
# #아이디는 진섭 , 비밀번호는 babo

# id = input("아이디 입력 : ")
# pw = input("비밀번호 입력 : ")

# if id == "진섭" and pw == "babo":
#     print("로그인 성공")
# else:
#     print("아이디 또는 비밀번호가 잘못 되었습니다.")

# # 파이썬에서 문자열 포함여부 확인하는 방법

# word = "나는 김진섭 입니다."
# if  '김진섭' in word :
#     print("있다")
# else:
#     print("없다")

# word = "나는 진섭이가 짝꿍일때 별로 였다."

# # word안에 동렬 이름이 없다라는 것을 확인할수 있는 코드 만드세요

# if '동렬' in word:
#     print("있다")
# else:
#     print("없다")

# if "동렬" not in word:
#     print("없다")

# #startswith() 함수 시작 문자열 비교
# word = "차도헌님께서 입장 하셨습니다."
# if word.startswith("이창호"):
#     print("신원 확인")
# else:
#     print("신원 확인 실패")

# #endswith() 함수  문자열 비교

# if word.endswith("하셨습니다."):
#     print("있다")

# #대소문자 변환
# word = "i like banana"
# print( word.upper() )#대문자
# print( word.lower() )#소문자
# print( word.title() )#대문자 -단어의 첫글자만

# #공백제거 - 개발시 필요필수( 이거 때문에 오류나면 골치 아픔)
# word = "  banana "
# print( word ) #공백제거 없이
# print( word.strip() )#양쪽 공백제거
# print( word.lstrip() )#왼쪽 공백제거
# print( word.rstrip() )#오른쪽 공백제거

# # 찾기
# word = "찬용이는  진섭이보다 지금이 좋다고 한다."
# print( word.find("진섭") ) # 있다면 윛치 반환 (인덱스) 없으면 -1
# # print( word.index("동렬")) # 인덱스반환, 없으면 에러

# # 문자열 바꾸기 .replace("현재 문자열에서 변경 할 문장열", "교체할 문자열")
# word = word.replace("찬용이","성현이")
# print(word)

# # 문자열 나누기 - 배열
# text = "도헌 - 지연 - 동렬 - 진섭"
# result = text.split(" - ")
# print(result)

# #배열을 하나의 문자열로 합치기
# text = " , ".join(result) #배열값 하나하나에 , 를 넣어서 하나의 문자열 만들기
# print(text)

# # 숫자냐 아니냐
# text = "12345"
# print( text.isnumeric() )# 문자열을 숫자로 변환하기전에 확인하는용도

# #문자 종류 확인
# text1 = "tomato"
# text2 = " "
# text3 = "사월22"
# print( text1.isalpha() ) #문자만 있는지?
# print( text2.isspace() ) #공백만 있는지?
# print( text3.isalnum() ) #문자 + 숫자냐

# #문자열 정렬
# text = "15"
# print( text.zfill(6)) # 함수 ()안에 자릿수 넣기
# print( text.rjust(4)) # 오른쪽 정렬
# print( text.ljust(4)) # 왼쪽 정렬

# # 문제 1. - 공백제거 와 소문자 변환을 하려면??
# #input으로 입력 받아서 공백 제거와 소문자 변환을 하세요

# text = input("소문자 변환기 : ")
# result=  text.strip().lower() 
# print(result)

# #문제 2. "행복,우울,기쁨,슬픔,화남"
# # 위 문자열을 나누어 보세요
# text = "행복,우울,기쁨,슬픔,화남"
# result = text.split(",")
# print(result)

# #문제3. 회원가입시 이메일 입력을 하는데 특정 주소만 가능하다.
# #naver.com , gmail.com, nate.com, daum.net
# # 위 4개만 가능하다
# # input으로 이메일을 입력받아서 가입 가능인지 불가능인지 출력

# # email = input("이메일 입력 : ").strip().lower()
# # result = email.split("@")
# # if result[1] == "naver.com" or result[1] == "gmail.com" or result[1] == "nate.com" or result[1] == "daum.net":
# #     print("가입가능")
# # else:
# #     print("가입불가능")


# email = input("이메일 입력 : ").strip().lower()
# # if email.endswith("naver.com"):
# #     print ("가입가능")
# # elif email.find("@gmail.com")!= -1:
# #     print("가입가능")
# # elif email.split("@")[1] == "nate.com":
# #     print("가입가능")
# # elif email.endswith("daum.net"):
# #     print("가입가능")
# # else:
# #     print("가입불가능")

# if "naver.com" not in email and "gmail.com" not in email and "nate.com" not in email and "daum.net" not in email:
#     print("가입불가능")
# else:
#     print("가입가능")    

#문제 4. 금액 계산하기 
# 각 업체별로 입금이 되었다. 총액이 얼마인지 출력하세요
쿠팡 = "135,900원"
네이버 = "540,000원"
오드론 = "2,340,000원"

쿠팡 = int(쿠팡.split("원")[0].replace(",",""))
네이버 = int(네이버.split("원")[0].replace(",",""))
오드론 = int(오드론.split("원")[0].replace(",",""))
result = 쿠팡+네이버+오드론
print(str(result)+"원")
print(f"합계: {result:,}원")
