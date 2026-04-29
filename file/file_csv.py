#csv - 쉼표로 구분된 데이터

import csv

# with open("file/test1.csv" , "r", encoding="utf-8") as f:
#     data= csv.reader(f)
#     print(data)

#     headers = next(data)
#     print(headers)

#     for row in data:
#         print(row)


# with open("file/test2.csv" , "w", newline="", encoding="utf-8")as f:
#     w = csv.writer(f)
#     w.writerow(["이름","생년","전화번호"])
#     w.writerow(["김유신","19990401","010-1234-1234"])


# with open("file/test2.csv" , "a", newline="", encoding="utf-8")as f:
#     w = csv.writer(f)
#     w.writerow(["이순신","19990401","010-3210-1234"])

# with open("file/test2.csv" , "r", newline="", encoding="utf-8")as f:
#     dic = csv.DictReader(f)

#     for row in dic:
#         print(row)

header = ["이름","나이","직업"]

with open("file/test2.csv","w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerow({"이름":"이순신","나이":"32","직업":"산업스파이"})
    w.writerow({"이름":"정약용","나이":"38","직업":"발명가"})