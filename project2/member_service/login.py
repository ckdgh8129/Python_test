from data import db



def login_process(id,pw):
       uid, upw = db.find_by_id(id)
       if uid==id and upw == pw:
           return "로그인 성공"
       else:
             return"로그인 실패"