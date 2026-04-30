import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    db = "ho",
    charset = "utf8"
)

cur = conn.cursor()

# cur.execute(쿼리문)
# conn.commit()


cur.execute("select * from item where item_qa >= %s", 
            (30,))

rows = cur.fetchall()
for row in rows:
    print(row)