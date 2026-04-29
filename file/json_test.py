import json


info = [
    {"name" : "김유신",
     "age" : 34,
     "addr" : "경주"
},
    {"name" : "이순신",
     "age" : 34,
     "addr" : "천안"}
]


with open("file/info.json","w", encoding="utf-8") as f:
    json.dump(info,f, ensure_ascii=False, indent=4)


# json 읽기
with open("file/info.json","r", encoding="utf-8") as f:
    member = json.load(f)

for user in member:
    print(user["name"],user["age"],user["addr"])

member.append({"name" :"문익점","age":25,"addr":"개경"})

with open("file/info.json","w", encoding="utf-8") as f:
    json.dump(member,f, ensure_ascii=False, indent=4)