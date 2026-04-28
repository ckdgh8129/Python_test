#아이디 길이 체크 함수, 비밀번호 최소 길이 체크 하는 함수
#아이디 길이는 4~12자 , 비밀번호는 최소 6자

def check_id(id):
    # if not (4 <= len(id) <= 12) :
    #     return "아이디는 4~12 자를 이용해주세요"
    # elif 6 > len(pw):
    #     return "비밀번호는 6자 이상을 이용해주세요"
    # else:
    #     return "가입 성공"
    return 4 <= len(id) <= 12

def check_pw(pw):
    return 6 <= len(pw)