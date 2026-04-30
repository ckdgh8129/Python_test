
print("오류??")

print(2+2)

try:
    print(10/0)
except:
    print("오류인가?")

# #예외 처리 
# try:
#     num = int(input("숫자입력 : "))
#     print(num)
# except Exception as e:
#     print(e)

# try:
#     오류가 예상되거나 사용자와 밀접한 코드
# except FileExistsError: #파일 오류


# except KeyError:    #키 오류


# try:
#     f= open("a.txt", "r")
# except FileNotFoundError:
#     print("파일이 없어요")

# finally:
#     f.close()
#     print("오류가 있어도 없어도 실행")

try:
    with open("a.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("파일이 없어요")

else:
    print("오류가 없을때만 실행")        

#숫자 입력을 잘 할때까지 계속 입력 받기
def check_age(num):
    if num < 0:
        raise Exception("음수는 입력할 수 없습니다")
    if num > 100:
        raise Exception("100 초과는 입력할 수 없습니다")

while True:
    try:
        num = int(input("나이 : "))
        check_age(num)
        break
    except ValueError as e:
        print(e)
    except:
        print("다시 입력하세요")


'''
    ValueError - 값이 잘못된 경우
    TypeError - 타입이 잘못된 경우
    ZeroDivisionError - 0을 나머지로 나머지는 경우
    IndexError - 인덱스 범위 초과
    KeyError - 딕셔너리 키 없는 경우
    NameError - 모듈, 함수, 변수가  없는 경우
    AttributeError - 속성/메서드 없는 경우
    FileNotFoundError - 파일 없는 경우
'''