
''' 
18396710_frame_12.json 에서 사람을 찾고 사람의 좌표를 출력하세요
'''

import json

with open("file/18396595_frame_12.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anno = data["frames"]["annotations"]

people = []
for ann in anno:
    if ann["category"]["code"] == "person":
        people.append(ann)
print(f"감지된 사람 수: {len(people)}")        

# people = [ann for ann in anno if ann["category"]["code"] == "person"]
# print(f"감지된 사람 수: {len(people)}")

for ann in anno:
    if ann["category"]["code"] == "person":
        label = ann["label"]
        print(f"좌표 x: {label['x']}, y: {label['y']}")

