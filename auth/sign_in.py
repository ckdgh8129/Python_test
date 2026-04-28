
#valid.py 사용 , db.py 사용 로그인 처리

#vaild.py 의 함수들을 통과해야 db.py를 통해 아이디 ,비밀번호 가져올수 있따.
import valid as _v
from data import db as _db

def signIn(id,pw):
    if not _v.valid_id(id) and _v.valid_pw(pw):
        print(" 아이디는 4~12자 입니다.")
    elif not _v.valid_pw(pw):
        print(" 비밀번호는 6자 이상 입니다.")
    else:
        uid,upw = _db.find_by_id(id)
        if uid == id and upw == pw:
            print("로그인 성공")
        else:
            print("아이디 또는 비밀번호를 잘못 입력하셨습니다.")
            