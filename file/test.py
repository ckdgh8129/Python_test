# 파일 입출력 - 프로그램에서 생성된 데이터들은 프로그램 종료시
# 메모리에서 사라진다. 필요한 데이터들을 남겨두기 위해서는 파일로 저장을 해야한다.
# 파일 입출력은 데이터를 저장하고 불러오는 방법이다.

#파일 쓰기 - 저장 , 파일 읽기 - 불러오기

# open("파일명", "모드") 모드= r: 읽기, w: 쓰기(덮어쓰기), a: 추가

# f=open("file/test1.txt", "w", encoding="utf-8")
# f.write("안녕하세요")
# f.close()
# text = input("입력 : ")

# with open("file/test1.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# 점심 = ["돈까스","짜장면","탕수육","떡볶이","감자탕" ]

# with open("file/test2.txt", "w", encoding="utf-8") as f:
#     for j in 점심:
#         f.write(f"{j}\n")
# 점심 = []
# with open("file/test2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         점심.append(line.replace("\n",""))
        
# print(점심)
    # t= f.readlines()
    # t2= f.readline()
    # t3= f.readline()
    # t4= f.readline()
    # t5= f.readline() 
    # t6= f.readline()

# print(t)    
# print(t2)
# print(t6=="")


# with open("file/test2.txt", "a", encoding="utf-8") as f:
#     f.write("라면")

# with open("file/image.jpg", "rb") as f:
#     img = f.read()
# print(img )

#문제 1. input 함수로 입력받은 값을 note.txt에 저장하시오
# text = input("입력 : ")
# with open("file/note.txt", "w", encoding="utf-8") as f:
    
#     f.write(text)

# 문제 2 . 회원가입을 받아서 파일로 저장하세요
#  회원 정보는 이름, 이메일, 비밀번호, 나이
# 파일 이름은 회원의 이메일 @ 앞부분이 파일 이름입니다.
# 파일 형식은 txt 입니다.
name = input("이름 입력 : ")
pw = input("비번 입력 : ")
email = input("이메일 입력 : ")
age = input("나이 입력 : ")
with open(f"file/{email.split('@')[0]}.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}\n")
    f.write(f"{pw}\n")
    f.write(f"{email}\n")
    f.write(f"{age}\n")
    #print(name,file=f)
    